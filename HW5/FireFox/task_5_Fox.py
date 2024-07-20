from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")


search = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')

# Write 1000

search.send_keys("1000")

sleep(3)

# Clear field

search.send_keys(Keys.CONTROL + "a")

search.send_keys(Keys.DELETE)

# write 999

search.send_keys("999")


sleep(2)

driver.quit()