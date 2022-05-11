from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.BasePage import Page
from PageObject.HomePage import HomePage


class LogIn(Page):
    username_field = '//*[@id="loginusername"]'
    password_field = '//*[@id="loginpassword"]'
    confirm_login = "//button[@onclick='logIn()']"
    cancel_login = "//button[@data-dismiss='modal' and @class='btn btn-secondary']"
    dialog_window = '//*[@id="logInModal"]/div/div'

    def input_username(self, username):
        self.find(self.username_field).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((By.XPATH, self.username_field), username))

    def input_password(self, password):
        self.find(self.password_field).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((By.XPATH, self.password_field), password))

    def click_confirm_login(self):
        self.click(self.confirm_login)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.find(HomePage.login_button)))

    def click_cancel_login(self):
        self.click(self.cancel_login)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.find(self.dialog_window)))
