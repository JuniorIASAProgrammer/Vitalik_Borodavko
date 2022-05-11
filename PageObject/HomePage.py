from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from CustomExpectedConditions.GridContainEC import product_grid_contain
from PageObject.BasePage import Page


class HomePage(Page):
    url = 'https://www.demoblaze.com/'
    login_button = '//*[@id="login2"]'
    logout_button = '//*[@id="logout2"]'
    laptops_button = '/html/body/div[5]/div/div[1]/div/a[3]'
    dell_laptop = '//*[@id="tbodyid"]/div[4]/div/div/h4/a'
    dialog_window = '// *[ @ id = "logInModal"]'
    cart_button = '//*[@id="navbarExample"]/ul/li[4]/a'
    product_on_grid = '//*[@class="hrefch"]'

    def click_login(self):
        self.click(self.login_button)

    def click_cart(self):
        self.click(self.cart_button)

    def click_laptops(self):
        self.click(self.laptops_button)

    def choose_laptop(self, product_model):
        WebDriverWait(self.driver, 10).until(product_grid_contain((By.XPATH, self.product_on_grid), product_model))
        self.click(self.dell_laptop)

    def click_logout(self):
        self.click(self.logout_button)
