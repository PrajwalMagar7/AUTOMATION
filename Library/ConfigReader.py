# import configparser

# def configRead(section, key):
#     config=configparser.ConfigParser()
#     config.read('./Configuration/Config.cfg')
#     return config.get(section, key)


# def ElementsRead():
#     config=configparser.ConfigParser()
#     config.read('./Configuration/Elements.cfg')    
#     return config.get(section, key)

# # print(configRead('Details','APP_URL'))   


import configparser

_config = configparser.ConfigParser()
_config.read('./Configuration/Config.cfg')

_elements = configparser.ConfigParser()
_elements.read('./Configuration/Elements.cfg')


def configRead(section, key):
    return _config.get(section, key)


def ElementsRead(section, key):
    return _elements.get(section, key)
