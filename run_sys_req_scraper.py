import sys
from src.scraping import SteamScraper

def run_sys_req_scraper(kwargs):
    ROOT_DIR = "./"
    sc = SteamScraper(ROOT_DIR)
    sc.scrape_data()
    sc.collect_sys_reqs(kwargs)

if __name__ == "__main__":
    print("Running scraper with params:\n{}".format(sys.argv))
    run_sys_req_scraper(sys.argv)