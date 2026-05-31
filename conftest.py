import sys
import os
import pytest
import allure
from utils.driver_factory import DriverFactory

# Agrega la raiz del proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def driver():
    """Fixture que crea y cierra el navegador por cada test"""
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Screenshot automatico en PASS y FAIL"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver:
            status = "PASS" if report.passed else "FAIL"
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"{status}_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
