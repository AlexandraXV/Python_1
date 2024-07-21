from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/dynamicid")



# click on the button


driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

sleep(3)

driver.quit()