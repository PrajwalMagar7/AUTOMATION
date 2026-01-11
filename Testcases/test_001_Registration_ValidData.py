from Base.InitiateDriver import startBrowser, closeBrowser
from Library.ConfigReader import ElementsRead
from Pages.RegistrationPage import RegistrationData
import pytest 


def dataGenerator():
    listData=[
        ['Ram','Sharma','Dec','3','2003','ram@gmail.com','12345678','Male'],
        ['Shyam','karki','Sep','10','1999','shyam@gmail.com','123456789','Male'],
        ['Sita','Pandey','Oct','26','1888','Sita@gmail.com','987654321','Female']
    ]

    return listData

@pytest.mark.parametrize('data',dataGenerator())
def test_validationRegistration(data):
    # driver=InitiateDriver.startBrowser()
    driver = startBrowser()
    register= RegistrationData(driver)
    register.enterFirstName(data[0])
    register.enterLastName(data[1])
    register.enterBirthMonth(data[2])
    register.enterBirthDay(data[3])
    register.enterBirthYear(data[4])
    register.enterGender(data[7])
    register.enterEmail(data[5])
    register.enterPassword(data[6])
    register.enterSubmit()

    # driver.find_element('name', ElementsRead('Registration','b_month')).send_keys('Nov')
    # driver.find_element('name', ElementsRead('Registration','b_day')).send_keys('07')
    # driver.find_element('name', ElementsRead('Registration','b_year')).send_keys('1977')
    # driver.find_element('name', ElementsRead('Registration','gen_xpath')).click()
    # driver.find_element('name', ElementsRead('Registration','mail_xpath')).send_keys('shyamcena00@gmail.com')
    # driver.find_element('name', ElementsRead('Registration','pass_xpath')).send_keys('1234567')


    # driver.find_element('xpath', "//input[@name='firstname']").send_keys('Ram')
    # driver.find_element('xpath', "//input[@name='lastname']").send_keys('Cena')
    # driver.find_element('name', 'birthday_month').send_keys('Nov')
    # driver.find_element('name', 'birthday_day').send_keys('007')
    # driver.find_element('name', 'birthday_year').send_keys('1977')
    # driver.find_element('xpath', "//input[@value='2']").click()
    # driver.find_element('xpath', "//input[@aria-label='Mobile number or email']").send_keys('ramcena@gmail.com')
    # driver.find_element('xpath', "//input[@aria-label='New password']").send_keys('12345')
    # driver.find_element('xpath', "//button[@type='submit']").click()

    
    closeBrowser()