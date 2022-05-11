from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, button):
        element = self.driver.find_element(by=By.XPATH, value=button)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        element.click()

    def find(self, element):
        return self.driver.find_element(by=By.XPATH, value=element)

    def find_all(self, element):
        return self.driver.find_elements(by=By.XPATH, value=element)

    def is_on_screen(self, element):
        return self.driver.find_element(by=By.XPATH, value=element).is_displayed()
