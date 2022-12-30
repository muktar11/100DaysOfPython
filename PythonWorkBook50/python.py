from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep 


FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL 
FB_PASSWORD = YOUR FACEBOOK PASSWORD 

chrome_driver_path = YOUR CHROME DRIVER PATH 
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath()
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath()
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email  = driver.find_element_by_xpath()
password = driver.find_element_by_xpath()

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.windw(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath()
allow_location_button.click()
notifications_button = driver.find_element_by_xpath()
notifications_button.click()
cookies = driver.find_element_by_xpath()
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath()like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup =driver.find_element_by_css_selector(".itsAmatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
driver.quit()