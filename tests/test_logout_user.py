from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from prerequisites.user_registartion import pre_registration
from locators import RegistrationLocators as RL
from locators import LoginLogoutLocators as LLL


class TestLogoutUser:

    def test_logout_user_logged_out(self, driver):
        email, password = pre_registration(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RL.PASS_INPUT).send_keys(password)
        driver.find_element(*LLL.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))
        driver.find_element(*LLL.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))

        WebDriverWait(driver, 1).until_not(expected_conditions.visibility_of_element_located(RL.PROFILE_NAME))
        assert driver.find_element(*RL.REGISTRATION_BUTTON).text == "Вход и регистрация"
