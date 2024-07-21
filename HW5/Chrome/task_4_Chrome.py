from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep (5)

driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p').click()

sleep(5)