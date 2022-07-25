import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('login info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def getHomePageTitle():
        homepagetitle = config.get('login info', 'homepage_title')
        return homepagetitle

    @staticmethod
    def getLoginPageTitle():
        loginpage_title = config.get('login info', 'loginpage_title')
        return loginpage_title

    @staticmethod
    def getPath():
        path = config.get('login info', 'login_data_file')
        return path

    @staticmethod
    def getURLopencart():
        url = config.get('login info', 'URL')
        return url

