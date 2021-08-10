from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.introduction.intro_page import IntroPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/intro_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestIntro(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.ip = IntroPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify D4 Logo Displays

    @pytest.mark.run(order=1)
    def test_D4_Logo_Displays(self):
        result = self.ip.verifyD4LogoDisplays()
        self.ts.markFinal("test_D4_Logo_Displays", result, "D4 Logo Displays")

    # Verify Return to Darkness Title Displays

    @pytest.mark.run(order=2)
    def test_RTD_Title_Displays(self):
        result = self.ip.verifyRTDTitleDisplays()
        self.ts.markFinal("test_RTD_Title_Displays", result, "Return to Darkness Title Displays")

    # Verify Video Element Displays
    # Research to see if there is a way to tell if the video actually plays
    @pytest.mark.run(order=3)
    def test_click_playIcon_video(self):
        self.ip.clickIntroPlayIcon()
        result = self.ip.verifyPlayIconVideo()
        self.ts.markFinal("test_click_playIcon_video", result, "Play Icon Plays Video")



