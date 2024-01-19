import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("/Users/soumyalakshmi/tools/chromedriver")

# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']").text)


def enter_value(name_enter):
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name_enter)
    driver.find_element(By.XPATH, "//input[@value='Alert']").click()


name_enter = "Soumya"
enter_value(name_enter)
time.sleep(10)
alert_var = driver.switch_to.alert  # alert_var  is the object for driver and focuses only on alert and will not
# focus on browser level
alertText = alert_var.text  # here the text I am grabbing and is assigned to another variable called grab_text
print(alertText)
# print(alert_var.text)
assert name_enter in alertText
alert_var.accept()  # will click on ok
# alert_var.dismiss() # will click on cancel
time.sleep(10)
# This is how we handle any browser based alerts.
