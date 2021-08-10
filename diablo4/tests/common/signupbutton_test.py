from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.common.signupbutton_page import SignUpButtonPage
from utilities.teststatus import TestStatus
import unittest
import pytest

#Run the page - pytest -s -v tests/common/signupbutton_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSignUpButton(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.sup = SignUpButtonPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Intro Sign Up Button Displays

    # @pytest.mark.run(order="#")
    def test_introSignUpButtonDisplays(self):
        #self.na.clickIntroSideNav()
        result = self.sup.verifyIntroSignUpButtonDisplays()
        self.ts.markFinal("test_introSignUpButtonDisplays", result, "Intro Sign Up Button Displays")

    #Verify Classes Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_classesSignUpButtonDisplays(self):
        self.sup.clickClassesSideNav()
        result = self.sup.verifyClassesSignUpButtonDisplays()
        self.ts.markFinal("test_classesSignUpButtonDisplays", result, "Classes Sign Up Button Displays")

    #Verify Gameplay Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_gameplaySignUpButtonDisplays(self):
        self.sup.clickGameplaySideNav()
        result = self.sup.verifyGameplaySignUpButtonDisplays()
        self.ts.markFinal("test_gameplaySignUpButtonDisplays", result, "Gameplay Sign Up Button Displays")

    #Verify World Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_worldSignUpButtonDisplays(self):
        self.sup.clickWorldSideNav()
        result = self.sup.verifyWorldSignUpButtonDisplays()
        self.ts.markFinal("test_worldSignUpButtonDisplays", result, "World Sign Up Button Displays")

    #Verify Story Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_storySignUpButtonDisplays(self):
        self.sup.clickStorySideNav()
        result = self.sup.verifyStorySignUpButtonDisplays()
        self.ts.markFinal("test_storySignUpButtonDisplays", result, "Story Sign Up Button Displays")

    #Verify Updates Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_updatesSignUpButtonDisplays(self):
        self.sup.clickUpdatesSideNav()
        result = self.sup.verifyUpdatesSignUpButtonDisplays()
        self.ts.markFinal("test_updatesSignUpButtonDisplays", result, "Updates Sign Up Button Displays")

    #Verify SignUp Page Sign Up Button Displays

    #@pytest.mark.run(order="#")
    def test_signupSignUpButtonDisplays(self):
        self.sup.clickSignUpSideNav()
        result = self.sup.verifySignUpSignUpButtonDisplays()
        self.ts.markFinal("test_signupSignUpButtonDisplays", result, "Sign Up Page Sign Up Button Displays")



