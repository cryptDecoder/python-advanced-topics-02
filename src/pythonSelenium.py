from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

# driver init
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
time.sleep(10)
driver.maximize_window()
driver.get("https://www.google.com/")
assert driver.title == driver.title
print(driver.current_url)
print(driver.title)

time.sleep(10)
driver.find_element_by_name("q").send_keys("python programming")
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
driver.close()
