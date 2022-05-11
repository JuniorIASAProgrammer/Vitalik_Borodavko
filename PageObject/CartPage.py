import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.BasePage import Page


class CartPage(Page):
    place_order = '//*[@id="page-wrapper"]/div/div[2]/button'
    fields = {
        'name_field': '//*[@id="name"]',
        'country_field': '//*[@id="country"]',
        'city_field': '//*[@id="city"]',
        'credit_card_field': '//*[@id="card"]',
        'month_field': '//*[@id="month"]',
        'year_field': '//*[@id="year"]'
    }
    cancel_button = '//*[@id="orderModal"]/div/div/div[3]/button[1]'
    purchase_button = '//*[@id="orderModal"]/div/div/div[3]/button[2]'
    confirmation_pop_up = '/html/body/div[10]'
    ok_on_confirmation = '/html/body/div[10]/div[7]/div/button'
    animated_round = '.sa-icon.sa-success.animate::after'

    def click_place_order(self):
        self.click(self.place_order)

    def click_cancel(self):
        self.click(self.cancel_button)

    def click_purchase(self):
        self.click(self.purchase_button)

    def confirmation_on_screen(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.find(self.confirmation_pop_up)))
        return self.is_on_screen(self.confirmation_pop_up)

    def click_ok_on_confirmation(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ok_on_confirmation)))
        time.sleep(0.5)
        self.click(self.ok_on_confirmation)
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element((By.XPATH, self.confirmation_pop_up)))

    def fill_in_the_form(self, values):
        for key, value in values.items():
            self.driver.find_element(by=By.XPATH, value=self.fields[key]).send_keys(values[key])
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element_value((By.XPATH, self.fields[key]), values[key]))
