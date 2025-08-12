import pytest

from selenium import webdriver
from data import URLS


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URLS["home_page"])
    yield driver
    driver.quit()
