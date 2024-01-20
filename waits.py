import time
import common
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = common.get_driver()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(10)
products = driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(products))
assert (len(products)) > 0
common.product_select(products)
time.sleep(10)
