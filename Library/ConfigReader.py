import configparser

def configRead(section, key):
    config=configparser.ConfigParser()
    config.read('../Configuration/Config.cfg')
    return config.get(section, key)


def ElementsRead(section,key):
    config=configparser.ConfigParser()
    config.read('../Configuration/Elements.cfg')    
    return config.get(section, key)

# print(configRead('Details','APP_URL'))    