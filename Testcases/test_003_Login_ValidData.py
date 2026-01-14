from selenium.webdriver.common.by import By
from Base.InitiateDriver import startBrowser, closeBrowser

def test_validationLogin():
    driver = startBrowser()

    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("9809817344")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1234567")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    closeBrowser(driver)
