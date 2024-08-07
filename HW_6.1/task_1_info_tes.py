from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


def test_data_farm():
    driver.implicitly_wait(10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone.send_keys("+7985899998787")
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")

    job_position = driver.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.send_keys("QA")

    company = driver.find_element(
        By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")

    driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()
    assert "danger" in driver.find_element(
        By.CSS_SELECTOR, ".alert.py-2.alert-danger").get_attribute("class")

    assert "success" in driver.find_element(
        By.CSS_SELECTOR, ".alert.py-2.alert-success").get_attribute("class")

    driver.quit()
