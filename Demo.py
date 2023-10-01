from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("#### Starting ####")
driver = webdriver.Chrome()
driver.maximize_window()  
# driver.get("https://www.google.com/")
driver.get("file:///C:/Productivity/GIT/PySelenium/index.html")

time.sleep(3)

driver.find_element("name", "q").send_keys("world!!")
time.sleep(3)

driver.find_element("name", "btnK").send_keys(Keys.ENTER)
time.sleep(3)

x= driver.find_element("name", "a").text
print(x)

assert x == "Hello world!!"
driver.close()
print("#### Done ####")