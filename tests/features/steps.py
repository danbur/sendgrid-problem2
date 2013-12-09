from lettuce import *
from api_workshop_page import ApiWorkshopPage
import settings

@step('I am on the SendGrid API Workshop page')
def on_the_sendgrid_api_workshop_page(step):
    world.driver.get("http://sendgrid.com/docs/api_workshop.html")
    world.page = ApiWorkshopPage(world.driver)

@step('I enter my credentials in the login form')
def enter_credentials_in_login_form(step):
    world.page.enter_login(settings.LOGIN)
    world.page.enter_password(settings.PASSWORD)

@step(u'I open the send mail API form')
def open_send_mail_api_form(step):
    world.page.open_send_mail_api_form()

@step(u'I enter valid values in all the fields of the send mail API form')
def enter_values_in_send_mail_api_form(step):
    world.page.enter_to_email(settings.EMAIL)
    world.page.enter_to_name(settings.NAME)
    world.page.enter_from_email(settings.EMAIL)
    world.page.enter_from_name(settings.NAME)

@step(u'I click on the Try It button on the send mail API form')
def when_i_click_on_the_try_it_button_on_the_send_mail_api_form(step):
    assert False, 'This step must be implemented'
@step(u'the send mail API form should display a "([^"]*)" response')
def then_the_send_mail_api_form_should_display_a_group1_response(step, group1):
    assert False, 'This step must be implemented'
