from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class StoryPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    storySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[5]"
    meetYourMakerHeading = "//*[@id='AppContainer']/div[5]/div/div[2]/div/div[1]"
    meetYourMakerSubHeading = "//*[@id='AppContainer']/div[5]/div/div[2]/div/div[2]/div"
    storyCrossIcon = "//*[@id='AppContainer']/div[5]/div/a/div[3]/div/div"

    #METHODS

    def clickStorySideNav(self):
        self.waitForElement(self.storySideNav, locatorType="xpath")
        self.elementClick(self.storySideNav, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyMYMHeadingDisplays(self):
        self.waitForElement(self.meetYourMakerHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.meetYourMakerHeading, locatorType="xpath")

        return result

    def verifyMYMSubHeadingDisplays(self):
        self.waitForElement(self.meetYourMakerSubHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.meetYourMakerSubHeading, locatorType="xpath")

        return result

    def verifyStoryCrossIconDisplays(self):
        self.waitForElement(self.storyCrossIcon, locatorType="xpath")
        result = self.isElementDisplayed(self.storyCrossIcon, locatorType="xpath")

        return result