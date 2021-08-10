from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class D4LogoSmallPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    classesSmallD4Logo = "//*[@id='AppContainer']/div[4]/div[1]"
    gameplaySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[3]"
    gameplaySmallD4Logo = "//*[@id='AppContainer']/div[4]/div[1]"
    worldSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[4]"
    worldSmallD4Logo = "//*[@id='AppContainer']/div[4]/div[1]"
    storySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[5]"
    storySmallD4Logo = "//*[@id='AppContainer']/div[4]/div[1]"
    updatesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[6]"
    updatesSmallD4Logo = "//*[@id='AppContainer']/div[4]/div[1]"
    signUpSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[7]"
    signUpSmallD4Logo = "//*[@id='AppContainer']/div[3]/div[2]/div/div"

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

    def verifyClassesSmallD4LogoDisplays(self):
        self.waitForElement(self.classesSmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.classesSmallD4Logo, locatorType="xpath")

        return result

    def verifyGameplaySmallD4LogoDisplays(self):
        self.waitForElement(self.gameplaySmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.gameplaySmallD4Logo, locatorType="xpath")

        return result

    def verifyWorldSmallD4LogoDisplays(self):
        self.waitForElement(self.worldSmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.worldSmallD4Logo, locatorType="xpath")

        return result

    def verifyStorySmallD4LogoDisplays(self):
        self.waitForElement(self.storySmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.storySmallD4Logo, locatorType="xpath")

        return result

    def verifyUpdatesSmallD4LogoDisplays(self):
        self.waitForElement(self.updatesSmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.updatesSmallD4Logo, locatorType="xpath")

        return result

    def verifySignUpSmallD4LogoDisplays(self):
        self.waitForElement(self.signUpSmallD4Logo, locatorType="xpath")
        result = self.isElementDisplayed(self.signUpSmallD4Logo, locatorType="xpath")

        return result

