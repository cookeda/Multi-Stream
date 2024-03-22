from stream_package.stream_scraper import StreamScraper
import os



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
    scraper.fetch_page_content(url)