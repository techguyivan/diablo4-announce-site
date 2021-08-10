from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class ClassesPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    druidCrossIcon = "//*[@id='AppContainer']/div[5]/div/div[1]/div[4]/div/div[3]/button/div"
    druidPortrait = "//*[@id='AppContainer']/div[2]/div/div[5]/div/div/div/div/div/div[2]/div[1]"

    # METHODS

    def clickClassesSideNav(self):
        self.waitForElement(self.classesSideNav, locatorType="xpath")
        self.elementClick(self.classesSideNav, locatorType="xpath")

    def clickDruidCrossIcon(self):
        self.waitForElement(self.druidCrossIcon, locatorType="xpath")
        self.elementClick(self.druidCrossIcon, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyDruidPageDisplays(self):
        self.waitForElement(self.druidPortrait, locatorType="xpath")
        result = self.isElementDisplayed(self.druidPortrait, locatorType="xpath")

        return result