from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def collect_league_list(self, url: str):
        """
        Collects each h2 text similar to 'MLB Live Schedule' and the associated href from the page.

        Args:
            url (str): The URL of the webpage

        Returns:
            list of tuples: A list containing (h2 text, href) for each item found
        """
        self.fetch_page_content(url)
        
        league_data = []
        
        try:
            # Wait for the presence of the h2 element within div.clearfix
            wait = WebDriverWait(self.driver, 10)
            league_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='clearfix']/h2"))).text()
            #league_hrefs = wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//a[contains(@class, 'btn-block')]"))).href
            #print(league_element)
            
            for league_element in league_elements:
                # The text of the h2 element
                league_text = league_element.text
                
                # Find the parent div of the h2 element
                #parent_div = league_element.find_element(By.XPATH, "./..")
                # Within this parent div, find the a tag and get its href
                link_element = wait.until(EC.presence_of_element_located((By.XPATH, ".//a[contains(@class, 'btn-block')]")))
                league_href = link_element.text
                
                # Store the tuple of text and href
                league_data.append((league_text, league_href))
                
        except Exception as e:
            print(f"Error collecting league data from {url}: {e}")
        
        return league_data

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

class MatchupScraper:
    '''
    A class to scrape matchup data and manipulate data into the stream link.
    '''
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