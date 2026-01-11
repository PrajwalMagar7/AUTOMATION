from Library.ConfigReader import ElementsRead

class RegistrationData:

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, fname):
        self.driver.find_element("name", ElementsRead("Registration", "first_name")).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element("name", ElementsRead("Registration", "last_name")).send_keys(lname)

    def enterBirthMonth(self, month):
        self.driver.find_element("name", ElementsRead("Registration", "b_month")).send_keys(month)

    def enterBirthDay(self, day):
        self.driver.find_element("name", ElementsRead("Registration", "b_day")).send_keys(day)

    def enterBirthYear(self, year):
        self.driver.find_element("name", ElementsRead("Registration", "b_year")).send_keys(year)

    def enterGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element("xpath", "//input[@value='2']").click()
        else:
            self.driver.find_element("xpath", "//input[@value='1']").click()

    def enterEmail(self, email):
        self.driver.find_element("xpath", ElementsRead("Registration", "mail_xpath")).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element("xpath", ElementsRead("Registration", "pass_xpath")).send_keys(password)

    def enterSubmit(self):
        self.driver.find_element("xpath", "//button[@type='submit']").click()
