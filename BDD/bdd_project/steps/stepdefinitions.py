from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given(u'buyer is on the OLX homepage')     #should be same as of given in search.feature file
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get("https://www.olx.in/")


@when(u'buyer types product in searchbar')  #same as when
def step_impl(context):
    searchbar = context.driver.find_element(By.XPATH, "//input[@data-aut-id='searchBox']")
    searchbar.click()
    searchbar.clear()
    searchbar.send_keys("Cars")
    searchbar.send_keys(Keys.ENTER)


@then(u'search results should be displayed')    #same as then
def step_impl(context):
    assert context.driver.title.__contains__("Cars") and context.driver.url.__contains__("cars"), 'Search Failed'
    heading = context.driver.find_element(By.CSS_SELECTOR, "#main_content > div > div > section > div > div > h1")
    assert heading.text.__contains__("Cars"), 'Search Failed'