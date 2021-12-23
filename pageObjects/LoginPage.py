from selenium.webdriver.common.by import By


class LoginPage:
    textboxt_email_id = 'login'
    textbox_password_id = 'password'
    button_login_xpath = '//*[@id="wrapwrap"]/main/div/div/div/div/div[2]/div/form/div[3]/button'

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