from selenium import webdriver
import time
import pytest

page=webdriver.Chrome("C:/Users/91908/selenium_driver/chromedriver_win32/chromedriver.exe")
@pytest.fixture()
def setup():
    page.get("http://tutorialsninja.com/demo/")
    page.maximize_window()
    time.sleep(2)

