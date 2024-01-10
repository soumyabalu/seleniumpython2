import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("soumya")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abc123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "exampleFormControlSelect1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()   # css using ID
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text   # storing the  message obtained in a variable
# called message
print(message)
assert "Success" in message   # asserting that the message contains Success . if not the test ges fail
driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
time.sleep(10)  # will halt the execution for 10 second before going for further execution of the steps.
