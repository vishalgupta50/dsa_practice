"""
1. locating elements
        ID = "id"
        NAME = "name"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
"""

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoFindElementById():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, "login-input").send_keys("vishal@test.com")
        time.sleep(10)

    def find_element_by_xpath(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("vishal@test.com")
        time.sleep(10)

    def find_element_by_link_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        time.sleep(5)

    def find_element_by_partial_link_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Holida").click()
        time.sleep(5)

    def find_element_by_tag_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.find_element(By.TAG_NAME, "a").click()
        time.sleep(5)

    def find_elements_by_tag_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        s = ""
        for i in lista:
            s += i.text
        with open("anchor_element.txt", "w") as outfile:
            outfile.write(s)

find_element = DemoFindElementById()
find_element.find_elements_by_tag_name()


















