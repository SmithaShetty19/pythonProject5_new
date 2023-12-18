import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("****HomePageTitle started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****HomePageTitle passed******")
        else:
            self.driver.save_screenshot("../Screenshots/HomePageTitle.png")
            self.driver.close()
            self.logger.info("****HomePageTitle failed******")
            assert False


    def test_login(self, setup):
        self.logger.info("****Login started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****Login passed******")
        else:
            self.driver.save_screenshot("../Screenshots/login.png")
            self.driver.close()
            self.logger.info("****Login failed******")
            assert False
