from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class SecurePage(BasePage):

    HEADER        = (By.CSS_SELECTOR, "h2")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button")

    def is_loaded(self):
        return (
            self.is_visible(self.HEADER) and
            "/secure" in self.get_current_url()
        )

    def get_welcome_message(self):
        return self.get_text(self.FLASH_MESSAGE)
