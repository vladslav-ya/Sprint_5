import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import TEST_DATA
from locators import RegistrationLocators as RL


class TestUserRegistration:

    def test_user_registration_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(f"test_user{random.randint(1000, 9999)}@gmail.com")

        driver.find_element(*RL.PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))

        assert TEST_DATA["default_user_name"] in driver.find_element(*RL.PROFILE_NAME).text

    def test_user_registration_wrong_mask_not_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(f"test_user{random.randint(1000, 9999)}.com")

        driver.find_element(*RL.PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.ERROR_EMAIL))
        assert "inputError" in driver.find_element(*RL.ERROR_SUBMIT_PASS).get_attribute('class')

    def test_user_registration_already_exist_not_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(TEST_DATA["test_email"])

        driver.find_element(*RL.PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.ERROR_EMAIL))
        assert "inputError" in driver.find_element(*RL.ERROR_SUBMIT_PASS).get_attribute('class')
