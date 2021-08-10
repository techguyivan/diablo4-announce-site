from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class WorldPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    worldSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[4]"
    exploreSanctuaryHeading = "//*[@id='AppContainer']/div[5]/div/div[2]/div[1]/div/div[1]/div"
    worldText = "//*[@id='AppContainer']/div[5]/div/div[2]/div[1]/div/div[2]/div"
    beholdTheWorldIcon = "//*[@id='AppContainer']/div[5]/div/div[2]/a/div/div/div/button/div"

    #METHODS

    def clickWorldSideNav(self):
        self.waitForElement(self.worldSideNav, locatorType="xpath")
        self.elementClick(self.worldSideNav, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyESHeadingDisplays(self):
        self.waitForElement(self.exploreSanctuaryHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.exploreSanctuaryHeading, locatorType="xpath")

        return result

    def verifyWorldFlavorTextDisplays(self):
        self.waitForElement(self.worldText, locatorType="xpath")
        result = self.isElementDisplayed(self.worldText, locatorType="xpath")

        return result

    def verifyBTWIconDisplays(self):
        self.waitForElement(self.beholdTheWorldIcon, locatorType="xpath")
        result = self.isElementDisplayed(self.beholdTheWorldIcon, locatorType="xpath")

        return result

