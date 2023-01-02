"""


"""

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoBrowserMethods():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/homestays")
        print(driver.current_url)
        # driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[2]").click()
        # driver.back()
        # driver.maximize_window()
        # driver.forward()
        # driver.back()
        attribute_name = driver.find_element(By.XPATH, "//input[@id='BE_hotel_htsearch_btn']").get_attribute("data-trackcategory")
        driver.refresh()
        print(driver.title)
        print(attribute_name)
        time.sleep(5)
        driver.quit()
        # time.sleep(5)


demo = DemoBrowserMethods()
demo.find_element_by_id_and_name()