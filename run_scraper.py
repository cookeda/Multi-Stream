from stream_package.stream_scraper import StreamScraper
import os
from dotenv import load_dotenv


load_dotenv()
if __name__ == '__main__':

    # # User-Agent String
    custom_user_agent = str(os.getenv("USER_AGENT"))
    
    # # Brave Path
    custom_brave_path = str(os.getenv("BRAVE_PATH"))
    
    # URL String
    url = 'https://methstreams.com/here/'
    
    #Initialize scraper
    scraper = StreamScraper(user_agent=custom_user_agent, brave_path=custom_brave_path)
    
    #
    print(scraper.collect_league_list(url))