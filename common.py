from selenium import webdriver


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
