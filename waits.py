import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(10)
products = driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(products))
for product in products:
    if product = "Cucumber - 1 Kg":



time.sleep(10)



