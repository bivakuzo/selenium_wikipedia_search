from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

chrome_driver_path="chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
search_box = driver.find_element(By.NAME,"search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

time.sleep(10)