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

    # LOCATORS

    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    barbarianCrossIcon = "//*[@id='AppContainer']/div[5]/div/div[1]/div[4]/div/div[1]/button/div"
    barbarianPortrait = "//*[@id='AppContainer']/div[2]/div/div[5]/div/div/div/div/div/div[2]/div[1]"

    # METHODS

    def clickClassesSideNav(self):
        self.waitForElement(self.classesSideNav, locatorType="xpath")
        self.elementClick(self.classesSideNav, locatorType="xpath")

    def clickBarbarianCrossIcon(self):
        self.waitForElement(self.barbarianCrossIcon, locatorType="xpath")
        self.elementClick(self.barbarianCrossIcon, locatorType="xpath")

    # VERIFICATION METHODS

    def verifyBarbarianPageDisplays(self):
        self.waitForElement(self.barbarianPortrait, locatorType="xpath")
        result = self.isElementDisplayed(self.barbarianPortrait, locatorType="xpath")

        return result