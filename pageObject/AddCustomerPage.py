import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class AddCustomer:
    lnkcustomermainmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomermenuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnaddnew_xpath = "//a[@class='btn btn-primary']"
    txtboxemail_xpath = "//input[@id='Email']"
    txtboxpassword_xpath = "//input[@id='Password']"
    txtboxfirstname_xpath = "//input[@id='FirstName']"
    txtboxlastname_xpath = "//input[@id='LastName']"
    rdbtngendermale_xapth = "//input[@id='Gender_Male']"
    rdbtngenderfemale_xpath = "//input[@id='Gender_Female']"
    txtboxdob_xpath = "//input[@id='DateOfBirth']"
    txtboxcompanyname_xpath = "//input[@id='Company']"
    chkboxtaxexempt_xpath = "//input[@id='IsTaxExempt']"
    txtboxnewsletter_xpath = "//input[@aria-expanded='true']"
    txtboxcustomerrole_xpath = "//input[@class='k-input']"
    lstitemregistered_xpath = "//li[@id='95407c2a-a912-416a-ad32-47828acc3be5']"
    lstitemadministrators_xpath = "//li[normalize-space()='Administrators']"
    lstitemvendor_xpath = "//li[contains(text(),'Vendors')]"
    lstitemguests_xpath = "//li[normalize-space()='Guests']"
    lstitemforummoderators_xpath = "//li[normalize-space()='Forum Moderators']"
    drpdmngrofvendor_xpath = "//select[@id='VendorId']"
    chkboxactive_xpath = "//input[@id='Active']"
    txtareaadmincontent_xpath = "//textarea[@id='AdminComment']"
    btnsave_xpath = "//button[@name='save']"
    itemdelete = "// span[ @ title = 'delete']"

    def __init__(self, driver):
        self.driver = driver

    def clickon_customermenu(self):
        self.driver.find_element(By.XPATH, self.lnkcustomermainmenu_xpath).click()

    def clickon_custmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkcustomermenuitem_xpath).click()

    def clickon_addnew(self):
        self.driver.find_element(By.XPATH, self.btnaddnew_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txtboxemail_xpath).send_keys("email")

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txtboxpassword_xpath).send_keys("password")

    def set_firstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtboxfirstname_xpath).send_keys("fname")

    def set_lastname(self, lname):
        self.driver.find_element(By.XPATH, self.txtboxfirstname_xpath).send_keys("lname")

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdbtngendermale_xapth).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdbtngenderfemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdbtngendermale_xapth).click()
    def



