"""
Selenium steps to configure behave test scenarios
"""
import time

@When('I open the demo site - "{url}"')
def step(context, url):
    context.browser.get(url)

@Then('Select the desired location')
def step(context):
    context.browser.find_element_by_id('headlessui-listbox-button-1').click()
    context.browser.find_element_by_id('Bali').click()
    print('Location is selected as Bali.')

@Then('Select the number of guests')
def step(context):
    context.browser.find_element_by_id('headlessui-listbox-button-5').click()
    context.browser.find_element_by_id('2').click()
    print('Number of guests are selected.')

@Then('Search for the results')
def step(context):
    context.browser.find_element_by_xpath("//*[@id='search']").click()
    context.browser.implicitly_wait(3)

@Then('Select one of the hotels')
def step(context):
    context.browser.find_element_by_id('reserve-now').click()
    context.browser.implicitly_wait(3)

@Then('Proceed with the booking')
def step(context):
    context.browser.find_element_by_id('proceed').click()
    context.browser.implicitly_wait(3)
    print('Booking is confirmed.')

@Then('Download the invoice')
def step(context):
    context.browser.find_element_by_id('invoice').click()
    context.browser.implicitly_wait(3)
    print('Tests are run successfully!')
    context.browser.execute_script("lambda-status=passed")
