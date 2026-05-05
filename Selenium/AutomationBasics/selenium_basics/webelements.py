from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time

#Start Driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

#Text Input locator
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#Password Input locator
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

#Text Area locator
text_area = driver.find_element(By.NAME, "my-textarea")
text_area.clear()
text_area.send_keys("This is a sample message")

#Checkbox locator
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#Radio Button locator
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#Dropdown(select) locator
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#Multi-Select (dropdown (data list))
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys("New York")

#File Upload locator
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys(r"C:\Wipro Training\Selenium\AutomationBasics\selenium_basics\google_homepage_test.py")
#Range Slider locator
range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value=9", range_slider)

#Color Picker locator
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#00ff00")

#Date Picker locator
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

#Submit Button locator
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()


time.sleep(10)
driver.quit()