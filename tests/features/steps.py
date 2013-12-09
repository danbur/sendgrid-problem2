from lettuce import *
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import re
from api_workshop_page import ApiWorkshopPage
import settings

SUBJECT_VALUE = "SendGrid Code Test"
TEXT_VALUE = "This is the SendGrid Code Test"
HTML_VALUE = "<p>This is the <b>SendGrid</b> Code Test</p><br/><br/>"
HEADERS_VALUE = '{"X-Accept-Language": "en", "X-Mailer": "QuasiFoobar"}'
FILES_VALUE = "files[file1.doc]=example.doc"

def get_date():
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return format_date_time(stamp)

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
    world.page.enter_field_data("to", settings.EMAIL)
    world.page.enter_field_data("toname", settings.NAME)
    world.page.enter_field_data("x-smtpapi", '{"category": "newuser"}')
    world.page.enter_field_data("from", settings.EMAIL)
    world.page.enter_field_data("fromname", settings.NAME)
    world.page.enter_field_data("subject", SUBJECT_VALUE)
    world.page.enter_field_data("text", TEXT_VALUE)
    world.page.enter_field_data("html", HTML_VALUE)
    world.page.enter_field_data("bcc", settings.EMAIL)
    world.page.enter_field_data("date", get_date())
    world.page.enter_field_data("headers", HEADERS_VALUE)
    world.page.enter_field_data("files", FILES_VALUE)

@step(u'I click on the Try It button on the send mail API form')
def when_i_click_on_the_try_it_button_on_the_send_mail_api_form(step):
    world.page.click_try_it()

@step(u'the send mail API form should display a "([^"]*)" response')
def then_the_send_mail_api_form_should_display_a_group1_response(step, group1):
    response = world.page.get_response_body()
    p = re.compile('^\s*{\s*"message":\s*"success"\s*}\s*$')
    assert p.match(response), 'Expecting "success" response, got: ' + \
        response

