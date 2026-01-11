from selenium.webdriver import Edge, Firefox,Chrome
from Library.ConfigReader import configRead

def startBrowser():
    global driver
    if configRead('Details', 'browser')=='firefox':
        driver = Firefox()
    elif configRead('Details', 'browser')=='edge':
        driver = Edge()    
    else:
        driver = Chrome()

    driver.get(configRead('Details','APP_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()    