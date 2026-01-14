# from selenium.webdriver import Edge, Firefox
# from Library.ConfigReader import configRead

# def startBrowser():
#     global driver
#     if configRead('Details', 'browser')=='firefox':
#         driver = Firefox()
#     elif configRead('Details', 'browser')=='edge':
#         driver = Edge()    
#     else:
#         driver = Firefox()

#     driver.get(configRead('Details','APP_URL'))
#     driver.maximize_window()
#     return driver

# def closeBrowser():
#     driver.close()    


from selenium.webdriver import Firefox, Edge
from Library.ConfigReader import configRead

def startBrowser():
    browser = configRead('Details', 'browser').lower()

    if browser == 'firefox':
        driver = Firefox()
    elif browser == 'edge':
        driver = Edge()
    else:
        driver = Firefox()

    driver.get(configRead('Details', 'APP_URL'))
    driver.maximize_window()
    return driver


def closeBrowser(driver):
    if driver:
        driver.quit()
