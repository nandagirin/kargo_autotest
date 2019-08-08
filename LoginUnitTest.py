import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
#import HtmlTestRunner
import os

class LoginUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = '/home/nanda/selenium_tutorial/geckodriver-v0.24.0-linux64/geckodriver')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,3)
        self.driver.get("https://kargo.tech/shipper/welcome/login")
    
    def test_LoginByBtnClick(self):
        self.driver.get("https://shipper-dev.testing.kargo.tech/login")
        self.nameField = self.driver.find_element_by_id("render_phone_number-field") # Find phone numb field
        self. passField = self.driver.find_element_by_id("render_textfield") # Find password field
        self.button = self.driver.find_element_by_id("button_component-button") # Find login button
        self.nameField.send_keys('85710311188')
        self.passField.send_keys('Ab1234')
        self.button.click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.home-page')))
        except TimeoutException:
            print("Invalid ID")
            return
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/a[5]').click() # Find profile button
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="profile_common-disabled_button"]'))) # Find logout button
        self.driver.find_element_by_xpath('//*[@id="profile_common-disabled_button"]').click() # Click the logout button
        time.sleep(2)

    def test_LoginByPressEnter(self):
        self.driver.get("https://shipper-dev.testing.kargo.tech/login")
        self.nameField = self.driver.find_element_by_id("render_phone_number-field")
        self.passField = self.driver.find_element_by_id("render_textfield")
        self.nameField.send_keys('85710311188')
        self.passField.send_keys('Ab1234', Keys.ENTER)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.home-page')))
        except TimeoutException:
            print("Invalid ID")
            return
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/a[5]').click() # Find profile button
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="profile_common-disabled_button"]'))) # Find logout button
        self.driver.find_element_by_xpath('//*[@id="profile_common-disabled_button"]').click() # Click the logout button
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    #testRunner=HtmlTestRunner.HTMLTestRunner(output=os.getcwd())
    unittest.main(verbosity=2)
