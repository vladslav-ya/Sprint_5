from selenium.webdriver.common.by import By


class RegistrationLocators:
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASS_INPUT = (By.NAME, "password")
    SUBMIT_PASS_INPUT = (By.NAME, "submitPassword")
    SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    CARDS = (By.CLASS_NAME, "card")
    USER_LOGO = (By.CSS_SELECTOR, "button[class='circleSmall']")
    PROFILE_NAME = (By.CSS_SELECTOR, "[class*='profileText']")
    ERROR_EMAIL = (By.XPATH, ".//span[text()='Ошибка']")
    ERROR_SUBMIT_PASS = (By.XPATH, ".//input[@name='submitPassword']/parent::div")

class LoginLogoutLocators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")

class AdvertisementLocators:
    PLACE_AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    POPUP_HEADER = (By.CSS_SELECTOR, "div[class*='popUp_titleRow']>h1[class='h1']")
    NAME_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.NAME, "price")
    SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    CATEGORY_DROP_BUTTON = (By.XPATH, ".//input[@name='category']/parent::div/button")
    CATEGORY_BUTTON = (By.XPATH, ".//button/span[text()='Садоводство']")
    CITY_DROP_BUTTON = (By.XPATH, ".//input[@name='city']/parent::div/button")
    CITY_BUTTON = (By.XPATH, ".//button/span[text()='Казань']")
    CONDITION_RADIO_BUTTON = (By.XPATH, ".//input[@value='Б/У']/parent::div/div[contains(@class, 'radio')]")
    USERS_AD_NAME = (By.XPATH, ".//div[@class='about']/h2[@class='h2']")

