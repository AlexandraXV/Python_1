from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


# 5 times click on the button Add Element 

button = driver.find_element(By.TAG_NAME, "button")

for x in range(5):
    button.click()

# sum button Delete
amount = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

print (len(amount))


sleep (3)