from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def run():
    # Enable headless mode
    firefox_options = Options()
    firefox_options.add_argument("--headless") 
    #selenium driver 
    #selenium request
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    time.sleep(1)
    accept_condiction = driver.find_element(By.CSS_SELECTOR, "button#L2AGLb")
    accept_condiction.click()
    #get all cookies 
    cookies = driver.get_cookies()


