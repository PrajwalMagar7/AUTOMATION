from Base.InitiateDriver import startBrowser, closeBrowser

def test_validationLogin():
    driver = startBrowser()
    driver.find_element('xpath', "//input[@type='text']").send_keys("9809817344")
    driver.find_element('xpath', "//input[@type='password']").send_keys("1234567")
    driver.find_element('xpath', "//button[@type='submit']").click()
    closeBrowser()