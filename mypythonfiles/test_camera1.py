from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains
from conftest import page

def test_camera(setup):
    desk=page.find_element_by_xpath('//*[text()="Desktops"]')
    desk.click()
    action=ActionChains(page)
    action.move_to_element(desk).perform()
    time.sleep(2)
    showall=page.find_element_by_xpath('//*[text()="Show All Desktops"]')
    showall.click()
    time.sleep(2)
    page.find_element_by_xpath('//*[text()="Cameras (2)"]').click()
    time.sleep(1)
    page.find_element_by_xpath('//*[text()="Nikon D300"]').click()
    time.sleep(1)
    page.find_element_by_id('button-cart').click()