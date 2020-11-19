from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import sys

from selenium.webdriver.support.wait import WebDriverWait

capabilities = {
    'browserName': 'chrome',
    'goog:chromeOptions': {'mobileEmulation': {'deviceName': f'{sys.argv[1]}'}},
    'version': '86.0',
    'enableVNC': True,
    'enableVideo': True
}

driver = webdriver.Remote(
    command_executor='http://159.65.133.63:4444/wd/hub',
    desired_capabilities=capabilities)

driver.get('https://xhamster.com/')
assert driver.title == 'Free Porn Videos & Sex Tube Movies at xHamster'

MENU_CATEGORIES = (By.CLASS_NAME, 'categories-list')
WebDriverWait(driver, 10).until(ec.invisibility_of_element_located(MENU_CATEGORIES),
                                message="Categories are visible")
driver.quit()
