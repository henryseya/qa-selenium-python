from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):

    # Localizadores
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE  = (By.ID, "flash")

    def navigate(self):
        self.driver.get(Config.BASE_URL + "/login")
        return self

    def enter_username(self, username: str):
        self.type(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)

    def is_flash_visible(self):
        return self.is_visible(self.FLASH_MESSAGE)
