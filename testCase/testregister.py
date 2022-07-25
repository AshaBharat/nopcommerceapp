from pageObject.registerpage import Register
from utilities.readProperties import ReadConfig


class TestRegister_TS_001:
    baseURL = ReadConfig.getURLopencart()


    def test_TC_RF_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.rp = Register(self.driver)
        self.rp.clickmyaccountmenu()
        self.rp.clickregisterlnk()
        assert True