import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.CSS_SELECTOR, ".forgot-password-link").click()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("abc123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("abc123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.XPATH, "(//a[@class='text-reset'])[1]").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("abc123")
driver.find_element(By.XPATH, "//input[@name='login']").click()
time.sleep(10)
