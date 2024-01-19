import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.find_element(By.XPATH, "//legend[text()='Radio Button Example']").text)
buttons = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")


def buttonClick(radio):
    for button in buttons:
        if button.get_attribute("value") == radio:
            button.click()
            assert button.is_selected()
            break


buttonClick("radio1")

driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("ind")
time.sleep(10)
print(driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']").text)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print(len(countries))


def auto_sugesion(country_name):
    for country in countries:
        if country.text == country_name:
            country.click()
            break


auto_sugesion("India")
assert driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value") == "India"
print(driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value"))

time.sleep(10)

print(driver.find_element(By.XPATH, "//legend[text()='Dropdown Example']").text)
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_value("option2")
assert driver.find_element(By.ID, "dropdown-class-example").get_attribute("value") == "option2"
time.sleep(10)

print(driver.find_element(By.XPATH, "//legend[text()='Checkbox Example']").text)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")


def check_box(option):
    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == option:
            checkbox.click()
            assert checkbox.is_selected()
            break


time.sleep(10)
check_box("option3")

print(driver.find_element(By.XPATH, "//legend[text()='Switch Window Example']").text)
driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
time.sleep(10)
