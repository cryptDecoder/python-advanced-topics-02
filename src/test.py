import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# driver initialization
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
time.sleep(10)
driver.get("https://www.google.com/")
assert driver.title == driver.title
print(driver.current_url)
print(driver.title)

# find element by name
driver.find_element_by_name('q').send_keys("Python selenium testing")
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
driver.close()