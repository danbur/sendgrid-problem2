from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30
IFRAME_BY = By.TAG_NAME
IFRAME_LOCATOR = "iframe"
CREDENTIALS_BY = By.ID
CREDENTIALS_LOCATOR = "credentials"
LOGIN_BY = By.XPATH
LOGIN_LOCATOR = "//form[@id='credentials']//div[label[text()='Username']]"\
    "/input"
PASSWORD_BY = By.XPATH
PASSWORD_LOCATOR = "//form[@id='credentials']//div[label[text()='Password']]"\
    "/input"
SECTIONS_BY = By.CSS_SELECTOR
SECTIONS_LOCATOR = "li.endpoint"
SECTION_NAME_BY = By.CSS_SELECTOR
SECTION_NAME_LOCATOR = ".title .name"
FORM_EXPANDER_BY = By.ID
FORM_EXPANDER_LOCATOR = "toggle-methods"
FORM_BY = By.TAG_NAME
FORM_LOCATOR = "form"
FIELD_ENTRY_BY = By.NAME
FIELD_ENTRY_LOCATOR_PREFIX = "params["
FIELD_ENTRY_LOCATOR_SUFFIX = "]"
TRY_IT_BY = By.ID
TRY_IT_LOCATOR = "Mail"
RESPONSE_BY = By.CLASS_NAME
RESPONSE_LOCATOR = "response"

class ApiWorkshopPage:
    def __init__(self, driver):
        self.__cache_mail_section = None
        self.driver = driver
        driver.switch_to_frame(driver.find_element(IFRAME_BY, IFRAME_LOCATOR))
        WebDriverWait(driver, TIMEOUT).until(\
            EC.presence_of_element_located(\
                (CREDENTIALS_BY, CREDENTIALS_LOCATOR)))

    def __mail_section(self):
        if self.__cache_mail_section:
            return self.__cache_mail_section

        sections = self.driver.find_elements(SECTIONS_BY, SECTIONS_LOCATOR)
        for section in sections:
            section_name = \
                section.find_element(SECTION_NAME_BY, SECTION_NAME_LOCATOR)
            if section_name.text == 'Mail':
                self.__cache_mail_section = section
                return section
        raise Exception("Mail section not found")

    def enter_login(self, login):
        self.driver.find_element(LOGIN_BY, LOGIN_LOCATOR).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(PASSWORD_BY, PASSWORD_LOCATOR)\
            .send_keys(password)

    def open_send_mail_api_form(self):
        self.driver.find_element(FORM_EXPANDER_BY, FORM_EXPANDER_LOCATOR)\
            .click()
        form = self.__mail_section().find_element(FORM_BY, FORM_LOCATOR)
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of(form))

    def enter_field_data(self, field, value):
        locator = FIELD_ENTRY_LOCATOR_PREFIX + field + \
            FIELD_ENTRY_LOCATOR_SUFFIX
        self.__mail_section().find_element(FIELD_ENTRY_BY, locator).\
            send_keys(value)

    def click_try_it(self):
        self.driver.find_element(TRY_IT_BY, TRY_IT_LOCATOR).click()
        WebDriverWait(self.driver, TIMEOUT).until(\
            EC.presence_of_element_located(\
                (RESPONSE_BY, RESPONSE_LOCATOR)))

    def get_response_body(self):
        return self.__mail_section()\
            .find_element(RESPONSE_BY, RESPONSE_LOCATOR).text
