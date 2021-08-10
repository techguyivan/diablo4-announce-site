from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.signup.signup_page import SignUpPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/signup_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSignUp(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.sup = SignUpPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Sign Up Heading Displays

    #@pytest.mark.run(order=#)
    def test_SignUpHeadingDisplays(self):
        self.sup.clickSignUpSideNav()
        result = self.sup.verifySignUpHeadingDisplays()
        self.ts.markFinal("test_SignUpHeadingDisplays", result, "Sign Up Heading Displays")

    # Verify Sign Up Paragraph Displays

    # @pytest.mark.run(order=#)
    def test_SignUpParagraphDisplays(self):
        self.sup.clickSignUpSideNav()
        result = self.sup.verifySignUpParagraphDisplays()
        self.ts.markFinal("test_SignUpParagraphDisplays", result, "Sign Up Paragraph Displays")

    # Verify Sign Up Button Displays

    # @pytest.mark.run(order=#)
    def test_SignUpButtonDisplays(self):
        self.sup.clickSignUpSideNav()
        result = self.sup.verifySignUpButtonDisplays()
        self.ts.markFinal("test_SignUpButtonDisplays", result, "Sign Up Button Displays")

    # Verify Sign Up Button routes to login page

    # @pytest.mark.run(order=#)
    def test_ClickSignUpButton(self):
        self.sup.clickSignUpSideNav()
        self.sup.clickSignUpButton()
        result = self.sup.verifyBlizzLogoLoginDisplays()
        self.ts.markFinal("test_ClickSignUpButton", result, "Sign Up Button Routes to Login Page")