import json
import pytest
import allure
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def load_test_data():
    with open("test-data/users.json", encoding="utf-8-sig") as f:
        return json.load(f)


@allure.feature("Autenticacion")
class TestLogin:

    @pytest.mark.smoke
    @allure.story("Login exitoso")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Login con credenciales validas desde JSON externo")
    def test_login_exitoso(self, driver):
        data = load_test_data()
        user = data["valid_user"]

        login_page = LoginPage(driver)
        login_page \
            .navigate() \
            .enter_username(user["username"]) \
            .enter_password(user["password"]) \
            .click_login()

        secure_page = SecurePage(driver)
        assert secure_page.is_loaded(), \
            "El area segura debe estar cargada tras login exitoso"

    @pytest.mark.regression
    @allure.story("Login fallido")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Login fallido muestra error correcto desde JSON")
    @pytest.mark.parametrize("user", load_test_data()["invalid_users"])
    def test_login_fallido(self, driver, user):
        login_page = LoginPage(driver)
        login_page \
            .navigate() \
            .enter_username(user["username"]) \
            .enter_password(user["password"]) \
            .click_login()

        assert login_page.is_flash_visible(), \
            "El mensaje de error debe ser visible"
        assert user["expected_error"] in login_page.get_flash_message(), \
            f"Error esperado: {user['expected_error']}"
