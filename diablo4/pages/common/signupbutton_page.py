from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class SignUpButtonPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    introSignUpButton = "//*[@id='AppContainer']/div[4]/div"
    classesSignUpButton = "//*[@id='AppContainer']/div[4]/div[2]"
    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    gameplaySignUpButton = "//*[@id='AppContainer']/div[4]/div[2]"
    gameplaySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[3]"
    worldSignUpButton = "//*[@id='AppContainer']/div[4]/div[2]"
    worldSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[4]"
    storySignUpButton = "//*[@id='AppContainer']/div[4]/div[2]"
    storySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[5]"
    updatesSignUpButton = "//*[@id='AppContainer']/div[4]/div[2]"
    updatesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[6]"
    signupSignUpButton = "//*[@id='main-content']/div/div/div[2]/div/div[2]/div/div[1]"
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

    def verifyIntroSignUpButtonDisplays(self):
        self.waitForElement(self.introSignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.introSignUpButton, locatorType="xpath")

        return result

    def verifyClassesSignUpButtonDisplays(self):
        self.waitForElement(self.classesSignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.classesSignUpButton, locatorType="xpath")

        return result

    def verifyGameplaySignUpButtonDisplays(self):
        self.waitForElement(self.gameplaySignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.gameplaySignUpButton, locatorType="xpath")

        return result

    def verifyWorldSignUpButtonDisplays(self):
        self.waitForElement(self.worldSignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.worldSignUpButton, locatorType="xpath")

        return result

    def verifyStorySignUpButtonDisplays(self):
        self.waitForElement(self.storySignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.storySignUpButton, locatorType="xpath")

        return result

    def verifyUpdatesSignUpButtonDisplays(self):
        self.waitForElement(self.updatesSignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.updatesSignUpButton, locatorType="xpath")

        return result

    def verifySignUpSignUpButtonDisplays(self):
        self.waitForElement(self.signupSignUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.signupSignUpButton, locatorType="xpath")

        return result