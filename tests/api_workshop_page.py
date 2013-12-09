from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ApiWorkshopPage:
    def __init__(self, driver):
        self.driver = driver
        driver.switch_to_frame(driver.find_element(By.TAG_NAME, "iframe"))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(\
                (By.ID, "credentials")))
