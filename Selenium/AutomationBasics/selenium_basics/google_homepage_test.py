"""
code for working with Google Homepage
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('What browser do you want you use(chrome or edge)?')

match(browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('Unknown browser - Not available \n Executing with default EDGE browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))        #service=Service(EdgeChromiumDriverManager().install()))

driver.get('https://www.google.com')    #get is selenium method for url to load in selenium



pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")

sleep(3)        #shouldn't be in the capstone project

driver.quit()