from selenium.webdriver.common.by import By
from Base.InitiateDriver import startBrowser, closeBrowser

def test_invalidationRegistration():
    driver = startBrowser()

    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys('@#$%')
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys('*&^%')

    driver.find_element(By.NAME, "birthday_month").send_keys('Nov')
    driver.find_element(By.NAME, "birthday_day").send_keys('007')
    driver.find_element(By.NAME, "birthday_year").send_keys('1977')

    driver.find_element(By.XPATH, "//input[@value='2']").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Mobile number or email']").send_keys('ramcena@gmail.com')
    driver.find_element(By.XPATH, "//input[@aria-label='New password']").send_keys('12345')

    closeBrowser(driver)
