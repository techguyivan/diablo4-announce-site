from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class SignUpPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    signUpSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[7]"
    signUpHeading = "//*[@id='main-content']/div/div/div[2]/div/div[1]"
    signUpParagraph = "//*[@id='main-content']/div/div/div[2]/div/div[2]/div/p"
    signUpButton = "//*[@id='main-content']/div/div/div[2]/div/div[2]/div/div[1]"
    blizzLogo = "/html/body/div/div/h1"

    # METHODS

    def clickSignUpSideNav(self):
        self.waitForElement(self.signUpSideNav, locatorType="xpath")
        self.elementClick(self.signUpSideNav, locatorType="xpath")

    def clickSignUpButton(self):
        self.waitForElement(self.signUpButton, locatorType="xpath")
        self.elementClick(self.signUpButton, locatorType="xpath")

    # VERIFICATION METHODS

    def verifySignUpHeadingDisplays(self):
        self.waitForElement(self.signUpHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.signUpHeading, locatorType="xpath")

        return result

    def verifySignUpParagraphDisplays(self):
        self.waitForElement(self.signUpParagraph, locatorType="xpath")
        result = self.isElementDisplayed(self.signUpParagraph, locatorType="xpath")

        return result

    def verifySignUpButtonDisplays(self):
        self.waitForElement(self.signUpButton, locatorType="xpath")
        result = self.isElementDisplayed(self.signUpButton, locatorType="xpath")

        return result

    def verifyBlizzLogoLoginDisplays(self):
        self.waitForElement(self.blizzLogo, locatorType="xpath")
        result = self.isElementDisplayed(self.blizzLogo, locatorType="xpath")

        return result

