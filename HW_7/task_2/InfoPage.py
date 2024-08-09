from selenium.webdriver.common.by import By


class InfoPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_data_farm(self, first_name, last_name,
                       adress, email, phone, city, country, job_position, company):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys(adress)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

        assert "danger" in self.driver.find_element(
            By.CSS_SELECTOR, ".alert.py-2.alert-danger").get_attribute("class")

        assert "success" in self.driver.find_element(
            By.CSS_SELECTOR, ".alert.py-2.alert-success").get_attribute("class")
