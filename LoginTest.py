from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

class LoginTest():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = '/home/nanda/selenium_tutorial/geckodriver-v0.24.0-linux64/geckodriver')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,3)
    
    def test_LoginByBtnClick(self):
        self.driver.get("https://kargo.tech/shipper/welcome/login")
        self.nameField = self.driver.find_element_by_id("render_phone_number-field")
        self. passField = self.driver.find_element_by_id("render_textfield")
        self.button = self.driver.find_element_by_id("button_component-button")
        self.nameField.send_keys('85710311188')
        self.passField.send_keys('Tebetbarat04')
        self.button.click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.home-page')))
        except TimeoutException:
            print("Invalid ID")
            return
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/a[5]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/div/div[2]/span')))
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div[5]/div/div[3]/button/span[1]').click()
        time.sleep(2)

    def test_LoginByPressEnter(self):
        self.driver.get("https://kargo.tech/shipper/welcome/login")
        self.nameField = self.driver.find_element_by_id("render_phone_number-field")
        self.passField = self.driver.find_element_by_id("render_textfield")
        self.nameField.send_keys('85710311188')
        self.passField.send_keys('Tebetbarat05', Keys.ENTER)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.home-page')))
        except TimeoutException:
            print("Invalid ID")
            return
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/a[5]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/div/div[2]/span')))
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div[5]/div/div[3]/button/span[1]').click()
        time.sleep(2)
    
if __name__ == '__main__':
    loginTest = LoginTest()
    loginTest.test_LoginByBtnClick()
    loginTest.test_LoginByPressEnter()
    loginTest.driver.quit()

