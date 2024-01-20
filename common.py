from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    driver = webdriver.Chrome()
    return driver


def buttonClick(radio, buttons):
    for button in buttons:
        if button.get_attribute("value") == radio:
            button.click()
            assert button.is_selected()
            break


def auto_sugesion(country_name, countries):
    for country in countries:
        if country.text == country_name:
            country.click()
            break


def check_box(option, checkboxes):
    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == option:
            checkbox.click()
            assert checkbox.is_selected()
            break


def enter_value(name_enter, driver):
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name_enter)


def product_select(products):
    for product in products:
        product.find_element(By.XPATH, "//div[3]//button[text()='ADD TO CART']").click()
        # break    # if we add break after the iteration it will add only one product to cart
