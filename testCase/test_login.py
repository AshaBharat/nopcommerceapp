from pageObject.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    homepage_title = ReadConfig.getHomePageTitle()
    loginpage_title = ReadConfig.getLoginPageTitle()
    logger = LogGen.loggen()
    def test_homePageTitle(self, setup):
        self.logger.info("***********Test_001_login**************")
        self.logger.info("*************Verifying HomePage********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_homepage_title = self.driver.title
        if act_homepage_title == self.homepage_title:
            assert True
            self.driver.close()
            self.logger.info("********* HomePage successfully loaded **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********* HomePage Failed to load **********")
            assert False

    def test_login(self, setup):
        self.logger.info("******** Verifying Login *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_loginpage_title = self.driver.title
        if act_loginpage_title == self.loginpage_title:
            self.logger.info("********* Successfully Logged In **********")
            self.lp.clickLogout()
            self.driver.close()
            assert True
        else:
            self.logger.info("********* Failed To Log In **********")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.lp.clickLogout()
            self.driver.close()
            assert False






