from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    textboxt_email_id = 'login'
    textbox_password_id = 'password'
    button_login_xpath = '//*[@id="wrapwrap"]/main/div/div/div/div/div[2]/div/form/div[3]/button'
    list_so_xpath = "//td[text()='Request Proforma Invoice']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(
            self.textboxt_email_id).send_keys(username)

    def setPassword(self, username):
        self.driver.find_element_by_id(
            self.textbox_password_id).send_keys(username)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickSalesOrder(self):
        print('page is ready')
        self.driver.find_element_by_xpath(self.list_so_xpath).click()

