import requests
import bs4
import re
import pandas as pd
import numpy as np
import time
import os


class steam_scraper():
    def __init__(self, ROOT_DIR):
        self.ROOT_DIR = ROOT_DIR
        self.all_games_url = "https://store.steampowered.com/search/?term=&ignore_preferences=1&page="

        self.cpus = None
        self.cpus = self.initialize_cpu_df()

    # def get_game_name(self, page):
    #     return {"name":page.find("div", class_="apphub_AppName").text}

    def get_game_price(self, page):
        # TODO
        return {}

    def get_release_date(self, page):
        date_elem = page.find("div", class_="date")
        if date_elem is None:
            # In the case that the page is a hardware page, a different
            # format is required
            details = page.find("div", class_="details_block")
            if details is None:
                return {}
            date = details.text.split(':')[-1].strip()
        else:
            date = date_elem.text
        return {"release_date":date}

    def extract_system_reqs(self, li_elems, spec):
        out = {}
        for li in li_elems:
            text = li.text
            if not (':' in text):
                out[spec + "_misc"] = text
            else:
                text = text.split(':')
                out[spec + '_' + text[0].lower()] = text[-1].strip()
        return out

    def get_sys_reqs(self, page):
        out = {}

        # Find system requirements element
        system_reqs = page.find("div", class_="sysreq_content")
        if system_reqs is None:
            return out
        else:
            system_reqs = system_reqs[0]

        full_reqs = page.find("div", class_="game_area_sys_req_full")
        if full_reqs is None:
            # Get minimum system requirements
            raw_min_reqs = system_reqs.find("div", class_="game_area_sys_req_leftCol")
            if not(raw_min_reqs is None):
                raw_min_reqs = raw_min_reqs.find_all("li")
                min_reqs = self.extract_system_reqs(raw_min_reqs, "min")
                out.update(min_reqs)

            # Get recommended system requirements
            raw_rec_reqs = system_reqs.find("div", class_="game_area_sys_req_rightCol")
            if not(raw_rec_reqs is None):
                raw_rec_reqs = raw_rec_reqs.find_all("li")
                rec_reqs = self.extract_system_reqs(raw_rec_reqs, "rec")
                out.update(rec_reqs)
        else:
            # Get system requirements
            raw_reqs = full_reqs.find_all("li")
            reqs = self.extract_system_reqs(raw_reqs, "min")
            out.update(reqs)

        return out

    def get_game_info(self, url):
        max_tries = 10
        tries = 2

        page = requests.get(url)
        while tries < max_tries and not page.ok:
            print("Retrying({}) {}".format(tries, url))
            time.sleep(1)
            page = requests.get(url)
            tries += 1
        if not page.ok:
            raise Exception("Unable to fetch game page")
        content = bs4.BeautifulSoup(page.content, features="lxml")

        out = {}

        out.update(self.get_game_price(content))
        out.update(self.get_release_date(content))
        out.update(self.get_sys_reqs(content))

        return out

    def initialize_cpu_df(self):
        usecols = ["Processor_Number", "nb_of_Cores", "nb_of_Threads",
            "Processor_Base_Frequency", "Max_Turbo_Frequency"]
        return pd.read_csv(self.ROOT_DIR + "data/Intel_CPUs.csv", usecols=usecols)
    
    def get_cpu_specs(self, row):
        """
        NOTE: Current implementation just gets the first match in the CPU dataset.
                This should be redone later to deal with non-unique processor numbers.
        """
        target_cpu = re.findall(r"(i\d-\d+)", row)[-1]
        if len(target_cpu) == 0:
            return None
        match = self.cpus[self.cpus["Processor_Number"] == target_cpu].iloc[0]
        # Drop Processor_Number key to avoid duplicate data
        match = match.drop("Processor_Number")
        return match

    def get_hardware_specs(self, df):
        cpu_specs = df["rec_processor"].apply(self.get_cpu_specs)

        df[cpu_specs.keys().str.lower()] = cpu_specs
        
        return df

    def extract_search_result(self, search_elem):
        # Do this filter because the links embed what page of the
        # store the game was found on. This helps manage duplicate
        # entries later on.
        href = search_elem["href"]
        href = re.findall(r"(.*)\?", href)[0]

        title = search_elem.find("span", class_="title").text

        return {"name":title,
                "href":href}

    def extract_page_games(self, page):
        content = bs4.BeautifulSoup(page, features="lxml")
        search_results = content.find_all('a', class_="search_result_row")
        game_links = list(map(lambda elem:self.extract_search_result(elem), search_results))
        return game_links

    def get_last_page_num(self, page):
        page = bs4.BeautifulSoup(page.content, features="lxml")
        num = page.find("div", class_="search_pagination_right").find_all("a")[-2].text
        return int(num)

    def fetch_all_games(self):
        retries = 10
        out = []

        # Load the first results page to find the total page numbers
        link = self.all_games_url + '1'
        page = requests.get(link)
        last_page_num = self.get_last_page_num(page)
        print("Fetching {} pages".format(last_page_num))

        # Iterate over all pages
        for page_num in range(1, last_page_num + 1):
            # Load page page_num
            link = self.all_games_url + str(page_num)
            page = requests.get(link)

            print("Loading {}".format(link), end="\r")

            content = self.extract_page_games(page.content)
            if len(content) == 0:
                for _ in range(retries):
                    print("Retrying {}".format(link))
                    time.sleep(1)
                    page = requests.get(link)
                    content = self.extract_page_games(page.content)
                    if len(content) != 0:
                        break
                if len(content) == 0:
                    print("Unable to retrieve data for {}".format(link))

            out.append({
                "page":page_num,
                "href":link,
                "data":content
            })

        return out

    def extract_games(self, game_pages):
        self.games = pd.DataFrame(game_pages["data"].explode().to_list())    

    def scrape_data(self, update=False):
        if os.path.exists(self.ROOT_DIR + "data/game_pages.csv") and not update:
            self.game_pages = pd.read_csv(self.ROOT_DIR + "data/game_pages.csv")
            self.game_pages["data"] = self.game_pages["data"].apply(eval)
        else:
            # Get all pages with every game on steam
            print("Fetching games from steam store")
            self.game_pages = pd.DataFrame(self.fetch_all_games())
            self.game_pages.to_csv(self.ROOT_DIR + "data/game_pages.csv", index=False)

        if os.path.exists(self.ROOT_DIR + "data/steam_games.csv") and not update:
            self.games = pd.read_csv(self.ROOT_DIR + "data/steam_games.csv")
        else:
            # Explode out the games from the fetched pages
            print("Extracting games from store pages")
            self.extract_games(self.game_pages)
            self.games.to_csv(self.ROOT_DIR + "data/steam_games.csv", index=False)