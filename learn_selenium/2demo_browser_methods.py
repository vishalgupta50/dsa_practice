"""

Operation	        Command	                                        Method/Property	  Description
Navigate to	        driver.get("https://training.rcvacademy.com")	Method	          Open the URL in browser session
Get Current URL	    driver.current_url	                            Property	      read the current URL from the browser’s address bar
Back	            driver.back()	                                Method	          Press the browser’s back button
Forward	            driver.forward()	                            Method	          Press the browser’s forward button
Refresh Page	    driver.refresh()	                            Method	          Refresh the current page
Get Page Title	    driver.title	                                Property	      read the current page title from the browser
Maximize Window	    driver.maximize_window()	                    Method	          Enlarges the window. For most operating systems, the window will fill the screen, without blocking the operating system’s own menus and toolbars.
Minimize Window	    driver.minimize_window()	                    Method	          Minimizes the window of current browsing context. The exact behavior of this command is specific to individual window managers.
Full screen window	driver.fullscreen_window()	                    Method	          Fills the entire screen, similar to pressing F11 in most browsers.

Closing a window    driver.close()                                  Method	          Close the current window
or tab

Quitting the        driver.quit()	                                Method	          Close all the windows and tabs associated with that WebDriver session
browser at the
end of a session


driver.get("https://training.rcvacademy.com")
driver.current_url
driver.back()
driver.forward()
driver.refresh()
driver.title
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.close()
driver.quit()


"""

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoBrowserMethods():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        print(driver.current_url)
        driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[2]").click()
        driver.back()
        driver.maximize_window()
        driver.forward()
        driver.back()
        driver.find_element(By.XPATH, "//span[normalize-space()='Visa']").click()
        driver.refresh()
        print(driver.title)
        time.sleep(5)
        driver.quit()
        # time.sleep(5)


demo = DemoBrowserMethods()
demo.find_element_by_id_and_name()