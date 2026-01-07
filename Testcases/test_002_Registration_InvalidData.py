from Base.InitiateDriver import startBrowser, closeBrowser

def test_invalidationRegistration():
    driver = startBrowser()
    driver.find_element('xpath', "//input[@name='firstname']").send_keys('@#$%')
    driver.find_element('xpath', "//input[@name='lastname']").send_keys('*&^%')
    driver.find_element('name', 'birthday_month').send_keys('Nov')
    driver.find_element('name', 'birthday_day').send_keys('007')
    driver.find_element('name', 'birthday_year').send_keys('1977')
    driver.find_element('xpath', "//input[@value='2']").click()
    driver.find_element('xpath', "//input[@aria-label='Mobile number or email']").send_keys('ramcena@gmail.com')
    driver.find_element('xpath', "//input[@aria-label='New password']").send_keys('12345')
    closeBrowser()
