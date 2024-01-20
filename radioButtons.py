import time
import common

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = common.get_driver()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.find_element(By.XPATH, "//legend[text()='Radio Button Example']").text)
buttons = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")

common.buttonClick("radio1", buttons)

print(driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']").text)
driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("ind")
time.sleep(10)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print(len(countries))

common.auto_sugesion("India", countries)

print(driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value"))
assert driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value") == "India"

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
print(driver.find_element(By.XPATH, "//legend[text()='Element Displayed Example']").text)
assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='show-textbox']").click()
assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()  # used to check weather an
# element is displayed in the wb page or not

time.sleep(10)

print(driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']").text)


def enter_value(name_enter):
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name_enter)
    driver.find_element(By.XPATH, "//input[@value='Alert']").click()


enter_value("Soumya")
time.sleep(10)
