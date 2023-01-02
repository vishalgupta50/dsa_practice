import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoBrowserMethods():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://training.openspan.com/login")
        button_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(button_state)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("abcd@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("abcdsdf")
        button_state_new = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        driver.find_element(By.XPATH, "//input[@id='login_button']").click()
        print(button_state_new)
        time.sleep(5)


demo = DemoBrowserMethods()
demo.find_element_by_id_and_name()