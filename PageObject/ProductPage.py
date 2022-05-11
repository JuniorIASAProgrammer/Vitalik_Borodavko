from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.BasePage import Page


class ProductPage(Page):
    add_to_cart = '//*[@id="tbodyid"]/div[2]/div/a'

    def click_add_to_cart(self):
        self.click(self.add_to_cart)

    def click_ok_on_notification(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
