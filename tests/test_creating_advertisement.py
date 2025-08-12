from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import TEST_DATA
from locators import RegistrationLocators as RL
from locators import LoginLogoutLocators as LLL
from locators import AdvertisementLocators as ADL


class TestCreatingAdvertisement:

    def test_creating_advertisement_unauthorized(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON))
        driver.find_element(*ADL.PLACE_AD_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ADL.POPUP_HEADER))
        assert driver.find_element(*ADL.POPUP_HEADER).text == "Чтобы разместить объявление, авторизуйтесь"


    def test_creating_advertisement_published(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.REGISTRATION_BUTTON)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.EMAIL_INPUT))
        driver.find_element(*RL.EMAIL_INPUT).send_keys(TEST_DATA["test_email"])
        driver.find_element(*RL.PASS_INPUT).send_keys(TEST_DATA["test_password"])
        driver.find_element(*LLL.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.USER_LOGO))

        driver.find_element(*ADL.PLACE_AD_BUTTON).click()

        driver.find_element(*ADL.NAME_INPUT).send_keys(TEST_DATA["ad_name"])
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*ADL.DESCRIPTION_INPUT))
        driver.find_element(*ADL.DESCRIPTION_INPUT).send_keys(TEST_DATA["ad_description"])
        driver.find_element(*ADL.PRICE_INPUT).send_keys(TEST_DATA["ad_price"])

        driver.find_element(*ADL.CATEGORY_DROP_BUTTON).click()
        driver.find_element(*ADL.CATEGORY_BUTTON).click()

        driver.find_element(*ADL.CITY_DROP_BUTTON).click()
        driver.find_element(*ADL.CITY_BUTTON).click()

        driver.find_element(*ADL.CONDITION_RADIO_BUTTON).click()

        driver.find_element(*ADL.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RL.CARDS))
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RL.USER_LOGO)).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ADL.USERS_AD_NAME)).text == TEST_DATA["ad_name"]
