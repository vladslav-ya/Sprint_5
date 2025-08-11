import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import RegistrationLocators as RL
from locators import LoginLogoutLocators as LLL


def pre_registration(driver):
    email = f"test_user{random.randint(1000, 9999)}@gmail.com"
    password = "123456"

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.NO_ACCOUNT_BUTTON)).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
    driver.find_element(*RL.EMAIL_INPUT).send_keys(email)

    driver.find_element(*RL.PASS_INPUT).send_keys(password)
    driver.find_element(*RL.SUBMIT_PASS_INPUT).send_keys(password)
    driver.find_element(*RL.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))
    driver.find_element(*LLL.LOGOUT_BUTTON).click()
    return email, password
