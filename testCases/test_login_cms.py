import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import logging as L


class Test_001_Login:
    baseUrl = 'https://demo-cms.62trade.com/web/login'
    baseUrlWeb = 'https://demo-web.62trade.com/'
    username_admin = 'admin'
    username_seller = 'pauziah@enablr.id'
    username_forwarder = 'zeepaw01@gmail.com'
    username_buyer = 'fauziahfz216@gmail.com'
    password = 'Sinergi01!'

    # def test_homePageTitle(self, setup):
    #     # Call driver chrome
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     # Catch title page login
    #     act_title = self.driver.title
    #     self.driver.close()
    #     if act_title == '62 Trade':
    #         assert True
    #     else:
    #         assert False

    def test_login_web(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrlWeb)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.clickBtnLogin()

    # def test_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.driver.implicitly_wait(10)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username_admin)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     act_title = self.driver.title
    #     print(act_title)
    #     # Driver close yang buat error no dession ID, ini buat session jadi hilang
    #     # self.driver.close()
    #     if act_title == '62 Trade':
    #         self.driver.implicitly_wait(20)
    #         self.lp.clickSOAcceptFWD()
    #         self.driver.quit()
    #         # self.lp.clickSidebarMenu()
    #         # self.lp.clickRFQ()
    #         # self.lp.clickSalesOrder()
    #         # self.lp.clickAcceptOrder()
    #         # self.lp.clickAcceptOrderForwarder()
    #         # self.lp.clickEditProformaInvoice()
    #         # self.lp.clickChooseShippingMode()
    #         assert True
    #     else:
    #         assert False

