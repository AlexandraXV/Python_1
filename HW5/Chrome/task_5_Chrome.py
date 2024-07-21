from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")


search = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')

search.send_keys("1000")

sleep(3)

search.send_keys(Keys.CONTROL + "a")

search.send_keys(Keys.DELETE)

search.send_keys("999")


sleep(5)