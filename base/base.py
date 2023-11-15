from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProtoPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1400, 1000)

    def input_fill(self, locator, text):
        locator = (By.XPATH, locator)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(text)

    def btn_click(self, locator):
        locator = (By.XPATH, locator)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_attribute(self, locator, attribute):
        locator = (By.XPATH, locator)
        attribute_value = (
            WebDriverWait(self.driver, 10)
            .until(EC.element_to_be_clickable(locator))
            .get_attribute(attribute)
        )
        return attribute_value

    def get_text(self, locator):
        locator = (By.XPATH, locator)
        text_value = (
            WebDriverWait(self.driver, 10)
            .until(EC.element_to_be_clickable(locator))
            .text
        )
        return text_value

    def page_refresh(self):
        self.driver.refresh()

    def element_on_form(self, locator):
        locator = (By.XPATH, locator)
        element = None
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except:
            return False
        return element is not None


class Letter:
    def __init__(self, recipient, subject, message):
        self.recipient = recipient
        self.subject = subject
        self.message = message

    def __eq__(self, other):
        if isinstance(other, Letter):
            return (
                self.recipient == other.recipient
                and self.subject == other.subject
                and self.message == other.message
            )
        return False
