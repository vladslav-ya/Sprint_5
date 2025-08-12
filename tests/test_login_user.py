from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import TEST_DATA
from locators import RegistrationLocators as RL
from locators import LoginLogoutLocators as LLL


class TestLoginUser:

    def test_login_user_logged_in(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(TEST_DATA["test_email"])
        driver.find_element(*RL.PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*LLL.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))

        assert "User" in driver.find_element(*RL.PROFILE_NAME).text
