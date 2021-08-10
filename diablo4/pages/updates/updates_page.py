from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class UpdatesPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    updatesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[6]"
    updatesHeading = "//*[@id='main-content']/div/div/div[2]/div[1]/div/div/div[2]"
    newsBlockGrid = "//*[@id='main-content']/div/div/div[2]/div[2]/div"
    moreUpdatesLink = "//*[@id='main-content']/div/div/div[2]/div[2]/div/p/a"

    #METHODS

    def clickUpdatesSideNav(self):
        self.waitForElement(self.updatesSideNav, locatorType="xpath")
        self.elementClick(self.updatesSideNav, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyDevUpdatesHeadingDisplays(self):
        self.waitForElement(self.updatesHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.updatesHeading, locatorType="xpath")

        return result

    def verifyNewsGridDisplays(self):
        self.waitForElement(self.newsBlockGrid, locatorType="xpath")
        result = self.isElementDisplayed(self.newsBlockGrid, locatorType="xpath")

        return result

    def verifyMoreUpdatesLinkDisplays(self):
        self.waitForElement(self.moreUpdatesLink, locatorType="xpath")
        result = self.isElementDisplayed(self.moreUpdatesLink, locatorType="xpath")

        return result





