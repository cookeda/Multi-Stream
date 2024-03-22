from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class StreamScraper:
    """
    A class to encapsulate web scraping functionalities
    """
    
    def __init__(self, user_agent: str, brave_path: str):
        """
        Initializes the WebScraper with a user agent.

        Args:
            user_agent (str): The User-Agent string to use for HTTP requests.
            brave_path (str): Path to Brave browser
        """
        options = Options()
        options.binary_location = brave_path
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    def fetch_page_content(self, url: str):
        """Fetches the content of a webpage.

        Args:
            url (str): The URL of the webpage

        Returns:
            str: The HTML content
        """
        try:
            self.driver.get(url)
            time.sleep(15)
        except:
            print(f'Error fetching {url}')

    def close_browser(self):
        """
        Closes the web browser.
    
        Returns:
            None
        """
        self.driver.quit()
    
    #def open_browser(self):
        
    # def fetch_page_content(self, url: str) -> str:
    #     """Fetches the content of a webpage.

    #     Args:
    #         url (str): The URL of the webpage

    #     Returns:
    #         str: The HTML content
    #     """
    #     try: 
    #pass