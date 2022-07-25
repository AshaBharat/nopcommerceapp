from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.AddCustomerPage import AddCustomer
from pageObject.loginPage import Login
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login successful*******")

        self.logger.info("******* Add Customer Test starting  *******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickon_customermenu()
        self.addcust.clickon_custmenuitem()
        self.addcust.clickon_addnew()

        self.logger("******** Filling customer add details *********")
        self.addcust.set_email(self.email)






