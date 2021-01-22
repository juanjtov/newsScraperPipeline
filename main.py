import argparse

from common import config

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
