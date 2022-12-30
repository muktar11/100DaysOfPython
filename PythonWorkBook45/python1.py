from selenium import webdriver


chrome_driver_path = "/home/iberahim/Documents/chromedriver"
driver = webdriver.Chrome(exectuable_path=chrome_driver_path)

driver.get("htt[s://www.python.org/")
price = driver.find_element_by_id("priceblock-purprice")
print(price.text)

#search_bar = driver.find_element_by_name("q")
#print(search_bar.get_attribute("placeholder"))

#logo = driver.find.element_by_class_name("python-logo a")
#print(documentation_link.text)

driver.find_elements_by_xpath("")
driver.close()
driver.quit()

event_times = driver.find_elemnets_by_css_selector(".event-widget.time")
event_names = driver.find_element_by_css_selector(".event_widget.li-a")
events = {}

for n in range(len(event_times)):
    events[n]= {
        "time": event_times[n].text, 
        "name": event_names[n].text,
    }
    
print(time.next)

