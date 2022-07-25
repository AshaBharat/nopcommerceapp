from pageObject.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    homepage_title = ReadConfig.getHomePageTitle()
    loginpage_title = ReadConfig.getLoginPageTitle()
    path = ReadConfig.getPath()
    logger = LogGen.loggen()

    def test_ddt_login(self, setup):
        self.logger.info("*********** Test_002_DDT_login **************")
        self.logger.info("************* Verifying DDT Login ********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("no of rows", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(20)

            act_loginpage_title = self.driver.title

            if act_loginpage_title == self.loginpage_title:
                if self.exp == 'Pass':
                    self.lp.clickLogout()
                    self.logger.info("********* Successfully Logged In **********")
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info("********* Logged in for incorrect credentials **********")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_ddt_login.png")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_loginpage_title != self.loginpage_title:
                if self.exp == 'Pass':
                    self.logger.info("********* couldnot login for correct credentials **********")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_ddt_login.png")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("********* Not Logged in for incorrect credentials **********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("****** Login DDT test Passed *****")
            self.driver.close()
            assert True
        else:
             self.logger.info("****** Login DDT test Failed *****")
             self.driver.close()
             assert False

        self.logger.info("***** End Of Login DDT Test *****")
        self.logger.info('****** completed TC_LoginDDT_002 ****')




