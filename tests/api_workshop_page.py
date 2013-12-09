from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IFRAME_BY = By.TAG_NAME
IFRAME_LOCATOR = "iframe"
CREDENTIALS_BY = By.ID
CREDENTIALS_LOCATOR = "credentials"
LOGIN_BY = By.XPATH
LOGIN_LOCATOR = "//*[@id='credentials']//*[label[text()='Username']]/input"
PASSWORD_BY = By.XPATH
PASSWORD_LOCATOR = "//*[@id='credentials']//*[label[text()='Password']]""/input"

class ApiWorkshopPage:
    def __init__(self, driver):
        self.driver = driver
        driver.switch_to_frame(driver.find_element(IFRAME_BY, IFRAME_LOCATOR))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(\
                (CREDENTIALS_BY, CREDENTIALS_LOCATOR)))

    def enter_login(self, login):
        self.driver.find_element(LOGIN_BY, LOGIN_LOCATOR).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(PASSWORD_BY, PASSWORD_LOCATOR).\
            send_keys(password)
