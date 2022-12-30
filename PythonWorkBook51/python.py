from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 


PROMISED_DOWN = 150
PROMISED_UP =10
CHROME_DRIVER_PATH= YOUR CHROME DRIVER PATH 
TWITTER_EMAIL = YOUR TWITTER EMAIL 
TWITTER_PASSWORD = YOUR TWITTER PASSWORD 

class InternetSpeedTwitterBott:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0 
        self.up = 0
        self.down = 0 

    def get_internet_speed(self):
        self.driver("https://www.speedtest.net/")
        # accept_button = self.driver.find_element_by_id("")
        # accept_button.click()
        # time.sleep(3)

        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath()
        self.down = self.driver.find_element_by_xpath()
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_xpath()
        password = self.driver.find_element_by_cpath()
        email.send_keys(TWITTER_PASSWORD)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep2(2)
        password.send_keys(Keys.Enter)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath()
        tweet = f""
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button =self.driver.find_element_by_xpath()
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBott(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
