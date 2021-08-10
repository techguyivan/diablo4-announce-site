from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.common.audioicon_page import AudioIconPage
from utilities.teststatus import TestStatus
import unittest
import pytest

# Run this page -  pytest -s -v tests/common/audioicon_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestAudioIcon(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.ai = AudioIconPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Intro Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_introAudioIconDisplays(self):
        # self.ai.clickIntroSideNav()
        result = self.ai.verifyAudioIconDisplays()
        self.ts.markFinal("test_introAudioIconDisplays", result, "Intro Audio Icon Displays")

    #Verify Classes Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_classesAudioIconDisplays(self):
        self.ai.clickClassesSideNav()
        result = self.ai.verifyAudioIconDisplays()
        self.ts.markFinal("test_classesAudioIconDisplays", result, "Classes Audio Icon Displays")

    #Verify Gameplay Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_gameplayAudioIconDisplays(self):
        self.ai.clickGameplaySideNav()
        result = self.ai.verifyAudioIconDisplays()
        self.ts.markFinal("test_gameplayAudioIconDisplays", result, "Gameplay Audio Icon Displays")

    #Verify World Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_worldAudioIconDisplays(self):
            self.ai.clickWorldSideNav()
            result = self.ai.verifyAudioIconDisplays()
            self.ts.markFinal("test_worldAudioIconDisplays", result, "World Audio Icon Displays")

    #Verify Story Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_storyAudioIconDisplays(self):
        self.ai.clickStorySideNav()
        result = self.ai.verifyAudioIconDisplays()
        self.ts.markFinal("test_storyAudioIconDisplays", result, "Story Audio Icon Displays")

    #Verify Updates Audio Icon Displays

    # @pytest.mark.run(order="#")
    def test_updatesAudioIconDisplays(self):
        self.ai.clickUpdatesSideNav()
        result = self.ai.verifyAudioIconDisplays()
        self.ts.markFinal("test_updatesAudioIconDisplays", result, "Updates Audio Icon Displays")

    #Verify Sign Up Audio Icon Displays

    #@pytest.mark.run(order="#")
    def test_signUpAudioIconDisplays(self):
            self.ai.clickSignUpSideNav()
            result = self.ai.verifyAudioIconDisplays()
            self.ts.markFinal("test_signUpAudioIconDisplays", result, "Sign Up Audio Icon Displays")



    #FIGURE OUT TEST TO VERIFY SOUND PLAYS