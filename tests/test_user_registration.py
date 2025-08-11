import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from prerequisites.user_registartion import pre_registration
from locators import RegistrationLocators as RL


class TestUserRegistration:

    def test_user_registration_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(f"test_user{random.randint(1000, 9999)}@gmail.com")

        driver.find_element(*RL.PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))

        assert "User" in driver.find_element(*RL.PROFILE_NAME).text

    def test_user_registration_wrong_mask_not_registered(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(f"test_user{random.randint(1000, 9999)}.com")

        driver.find_element(*RL.PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.ERROR_EMAIL))
        assert "inputError" in driver.find_element(*RL.ERROR_SUBMIT_PASS).get_attribute('class')

    def test_user_registration_already_exist_not_registered(self, driver):
        pre_registration(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(f"test_user{random.randint(1000, 9999)}.com")

        driver.find_element(*RL.PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys("123456")
        driver.find_element(*RL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.ERROR_EMAIL))
        assert "inputError" in driver.find_element(*RL.ERROR_SUBMIT_PASS).get_attribute('class')
