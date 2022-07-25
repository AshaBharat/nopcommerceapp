from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = r"https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
driver.get(url)
driver.maximize_window()