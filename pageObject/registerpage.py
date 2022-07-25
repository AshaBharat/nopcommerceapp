from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class Register:
    menu_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_xpath = "//a[text()='Register']"

    def __init__(self, driver):
        self.driver = driver

    def clickmyaccountmenu(self):
        self.driver.find_element(By.XPATH, self.menu_myaccount_xpath).click()

    def clickregisterlnk(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()



