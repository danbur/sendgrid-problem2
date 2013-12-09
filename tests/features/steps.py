from lettuce import *
from selenium import webdriver

@before.each_scenario
def start_webdriver(scenario):
    world.driver = webdriver.Firefox()

#@after.each_scenario
#def quit_webdriver(scenario):
    #world.driver.quit()

@step(u'Given I am on the SendGrid API Workshop page')
def on_the_sendgrid_api_workshop_page(step):
    world.driver.get("http://sendgrid.com/docs/api_workshop.html")

@step(u'When I enter my credentials in the login form')
def when_i_enter_my_credentials_in_the_login_form(step):
    assert False, 'This step must be implemented'
@step(u'When I open the send mail API form')
def when_i_open_the_send_mail_api_form(step):
    assert False, 'This step must be implemented'
@step(u'When I enter valid values in all the fields of the send mail API form')
def when_i_enter_valid_values_in_all_the_fields_of_the_send_mail_api_form(step):
    assert False, 'This step must be implemented'
@step(u'When I click on the Try It button on the send mail API form')
def when_i_click_on_the_try_it_button_on_the_send_mail_api_form(step):
    assert False, 'This step must be implemented'
@step(u'Then the send mail API form should display a "([^"]*)" response')
def then_the_send_mail_api_form_should_display_a_group1_response(step, group1):
    assert False, 'This step must be implemented'
