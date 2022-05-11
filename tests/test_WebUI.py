from selenium import webdriver

from PageObject.CartPage import CartPage
from PageObject.HomePage import HomePage
from PageObject.Login import LogIn
from PageObject.ProductPage import ProductPage


path = 'drivers/chromedriver.exe'

USERNAME = "burunduk"
PASSWORD = "test"

personal_info = {
    'name_field': 'Vitalik',
    'country_field': 'Ukraine',
    'city_field': 'Kyiv',
    'credit_card_field': '4444 3333 2222 1111',
    'month_field': '07',
    'year_field': "23"
    }

laptop_model = 'Dell i7 8gb'

driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(10)

homePage = HomePage(driver)
login = LogIn(driver)
productPage = ProductPage(driver)
cartPage = CartPage(driver)


def test_open_page():
    driver.get(homePage.url)
    driver.maximize_window()


# Step 1 : Натиснути Log in та ведіть Логін та Пароль свого юзера -> нажміть кнопку Log in
def test_log_in():
    homePage.click_login()
    login.input_username(USERNAME)
    login.input_password(PASSWORD)
    login.click_confirm_login()


# Step 2 : Виберіть категорію Laptops
def test_choose_category():
    homePage.click_laptops()


# Step 3 : Виберіть Dell i7 8gb
def test_choose_product():
    homePage.choose_laptop(product_model=laptop_model)


# Step 4 : Як з'явиться окремо товар, натисныть кнопку Add to cart
def test_add_to_cart():
    productPage.click_add_to_cart()
    productPage.click_ok_on_notification()


# Step 5 : Перейдіть в Cart розділ та нажміть Place Order
def test_place_order():
    homePage.click_cart()
    cartPage.click_place_order()


# Step 6 : Заповніть поля Name, Country, City, Credit card, Month, Year та нажміть кнопку Purchase
def test_checkout():
    cartPage.fill_in_the_form(personal_info)
    cartPage.click_purchase()


# Step 7 : Перевірте що з'явився pop-up 'Thank you for your purchase!'
def test_confirmation():
    if not cartPage.confirmation_on_screen():
        raise Exception('Confirmation is not on screen')


def test_close_page():
    cartPage.click_ok_on_confirmation()
    homePage.click_logout()
    driver.quit()

