import sys
from src.scraping.scraping import SteamScraper

def run_sys_req_scraper(**kwargs):
    ROOT_DIR = "./"
    sc = SteamScraper(ROOT_DIR)
    sc.scrape_data()
    print(kwargs)
    sc.collect_sys_reqs(chunksize=kwargs.get("chunksize"), starting_chunk=kwargs.get("starting_chunk"), max_chunk=kwargs.get("max_chunk"))

if __name__ == "__main__":
    kwargs = {}
    for elem in sys.argv[1:]:
        key, val = elem.split('=')
        kwargs[key] = int(val)
    
    print("Running scraper with params:\n{}".format(kwargs))
    # run_sys_req_scraper(kwargs)
    run_sys_req_scraper(chunksize=kwargs.get("chunksize"), starting_chunk=kwargs.get("starting_chunk"), max_chunk=kwargs.get("max_chunk"))