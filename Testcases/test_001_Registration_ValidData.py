# from Base.InitiateDriver import startBrowser, closeBrowser
# from Library.ConfigReader import ElementsRead

# def test_validationRegistration():
#     driver = startBrowser()

#     driver.find_element('name', ElementsRead('Registration','fname')).send_keys('Shyam')
#     driver.find_element('name', ElementsRead('Registration','lname')).send_keys('Cena')
#     driver.find_element('name', ElementsRead('Registration','b_month')).send_keys('Nov')
#     driver.find_element('name', ElementsRead('Registration','b_day')).send_keys('07')
#     driver.find_element('name', ElementsRead('Registration','b_year')).send_keys('1977')
#     driver.find_element('name', ElementsRead('Registration','gen_xpath')).click()
#     driver.find_element('name', ElementsRead('Registration','mail_xpath')).send_keys('shyamcena00@gmail.com')
#     driver.find_element('name', ElementsRead('Registration','pass_xpath')).send_keys('1234567')


    # driver.find_element('xpath', "//input[@name='firstname']").send_keys('Ram')
    # driver.find_element('xpath', "//input[@name='lastname']").send_keys('Cena')
    # driver.find_element('name', 'birthday_month').send_keys('Nov')
    # driver.find_element('name', 'birthday_day').send_keys('007')
    # driver.find_element('name', 'birthday_year').send_keys('1977')
    # driver.find_element('xpath', "//input[@value='2']").click()
    # driver.find_element('xpath', "//input[@aria-label='Mobile number or email']").send_keys('ramcena@gmail.com')
    # driver.find_element('xpath', "//input[@aria-label='New password']").send_keys('12345')
    # driver.find_element('xpath', "//button[@type='submit']").click()
    # closeBrowser()



from selenium.webdriver.common.by import By
from Base.InitiateDriver import startBrowser, closeBrowser
from Library.ConfigReader import ElementsRead

def test_validationRegistration():
    driver = startBrowser()

    driver.find_element(By.NAME, ElementsRead('Registration','fname_name')).send_keys('Shyam')
    driver.find_element(By.NAME, ElementsRead('Registration','lname_name')).send_keys('Cena')

    driver.find_element(By.NAME, ElementsRead('Registration','b_month_name')).send_keys('Nov')
    driver.find_element(By.NAME, ElementsRead('Registration','b_day_name')).send_keys('07')
    driver.find_element(By.NAME, ElementsRead('Registration','b_year_name')).send_keys('1977')

    driver.find_element(By.XPATH, ElementsRead('Registration','gen_xpath')).click()
    driver.find_element(By.XPATH, ElementsRead('Registration','mail_xpath')).send_keys('shyamcena00@gmail.com')
    driver.find_element(By.XPATH, ElementsRead('Registration','pass_xpath')).send_keys('1234567')

    closeBrowser(driver)

