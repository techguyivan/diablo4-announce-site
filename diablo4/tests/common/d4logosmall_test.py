from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.common.d4logosmall_page import D4LogoSmallPage
from utilities.teststatus import TestStatus
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/d4logosmall_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class D4LogoSmall(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.d4LogoSmall = D4LogoSmallPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Small D4 Logo Displays on Classes Page

    #@pytest.mark.run(order="#")
    def test_ClassesSmallD4LogoDisplays(self):
        self.d4LogoSmall.clickClassesSideNav()
        result = self.d4LogoSmall.verifyClassesSmallD4LogoDisplays()
        self.ts.markFinal("test_ClassesSmallD4LogoDisplays", result, "Classes D4 Logo Displays")

    #Verify Small D4 Logo Displays on Gameplay Page

    #@pytest.mark.run(order="#")
    def test_GameplaySmallD4LogoDisplays(self):
        self.d4LogoSmall.clickGameplaySideNav()
        result = self.d4LogoSmall.verifyGameplaySmallD4LogoDisplays()
        self.ts.markFinal("test_GameplaySmallD4LogoDisplays", result, "Gameplay D4 Logo Displays")

    #Verify Small D4 Logo Displays on World Page

    #@pytest.mark.run(order="#")
    def test_WorldSmallD4LogoDisplays(self):
        self.d4LogoSmall.clickWorldSideNav()
        result = self.d4LogoSmall.verifyWorldSmallD4LogoDisplays()
        self.ts.markFinal("test_WorldSmallD4LogoDisplays", result, "World D4 Logo Displays")

    #Verify Small D4 Logo Displays on Story Page

    # @pytest.mark.run(order="#")
    def test_StorySmallD4LogoDisplays(self):
        self.d4LogoSmall.clickStorySideNav()
        result = self.d4LogoSmall.verifyStorySmallD4LogoDisplays()
        self.ts.markFinal("test_StorySmallD4LogoDisplays", result, "Story D4 Logo Displays")

    #Verify Small D4 Logo Displays on Updates Page

    #@pytest.mark.run(order="#")
    def test_UpdatesSmallD4LogoDisplays(self):
        self.d4LogoSmall.clickUpdatesSideNav()
        result = self.d4LogoSmall.verifyUpdatesSmallD4LogoDisplays()
        self.ts.markFinal("test_UpdatesSmallD4LogoDisplays", result, "Updates D4 Logo Displays")

    #Verify Small D4 Logo Displays on Sign Up Page

    #@pytest.mark.run(order="#")

    def test_SignUpSmallD4LogoDisplays(self):
        self.d4LogoSmall.clickSignUpSideNav()
        result = self.d4LogoSmall.verifySignUpSmallD4LogoDisplays()
        self.ts.markFinal("test_SignUpSmallD4LogoDisplays", result, "Sign Up D4 Logo Displays")

