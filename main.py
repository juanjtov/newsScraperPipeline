import argparse
import logging
logging.basicConfig(level=logging.INFO)

from common import config

#logger reference
logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    #acces the config already loaded
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Beggining scraper for {host}')

if __name__ == "__main__":
    #Define the args parser for the command line app
    parser = argparse.ArgumentParser()

    news_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help = 'The news site you want to scrape',
                        type=str,
                        choices=news_sites_choices)
    
    args = parser.parse_args()
    #passing the news_site to the function
    _news_scraper(args.news_site)
