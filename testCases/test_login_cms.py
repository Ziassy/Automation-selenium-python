import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import logging as L


class Test_001_Login:
    baseUrl = 'https://demo-cms.62trade.com/web/login'
    username = 'admin'
    password = 'Sinergi01!'

    def test_homePageTitle(self, setup):
        # Call driver chrome
        self.driver = setup
        self.driver.get(self.baseUrl)
        # Catch title page login
        act_title = self.driver.title
        self.driver.close()
        if act_title == '62 Trade':
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        # Driver close yang buat error no dession ID, ini buat session jadi hilang
        # self.driver.close()
        if act_title == '62 Trade':
            self.driver.implicitly_wait(20)
            self.lp.clickSalesOrder()
            assert True
        else:
            assert False

