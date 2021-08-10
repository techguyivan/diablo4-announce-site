from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class AudioIconPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    audioIcon = "//*[@id='AppContainer']/button[3]"
    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    gameplaySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[3]"
    worldSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[4]"
    storySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[5]"
    updatesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[6]"
    signUpSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[7]"

    #METHODS

    def clickClassesSideNav(self):
        self.waitForElement(self.classesSideNav,locatorType="xpath")
        self.elementClick(self.classesSideNav, locatorType="xpath")

    def clickGameplaySideNav(self):
        self.waitForElement(self.gameplaySideNav,locatorType="xpath")
        self.elementClick(self.gameplaySideNav, locatorType="xpath")

    def clickWorldSideNav(self):
        self.waitForElement(self.worldSideNav,locatorType="xpath")
        self.elementClick(self.worldSideNav, locatorType="xpath")

    def clickStorySideNav(self):
        self.waitForElement(self.storySideNav,locatorType="xpath")
        self.elementClick(self.storySideNav, locatorType="xpath")

    def clickUpdatesSideNav(self):
        self.waitForElement(self.updatesSideNav,locatorType="xpath")
        self.elementClick(self.updatesSideNav, locatorType="xpath")

    def clickSignUpSideNav(self):
        self.waitForElement(self.signUpSideNav,locatorType="xpath")
        self.elementClick(self.signUpSideNav, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyAudioIconDisplays(self):
        self.waitForElement(self.audioIcon, locatorType="xpath")
        result = self.isElementDisplayed(self.audioIcon, locatorType="xpath")

        return result