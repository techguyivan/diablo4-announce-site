from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.gameplay.gameplay_page import GameplayPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/gameplay_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestGameplay(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.gp = GameplayPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Abandon All Hope Heading Displays

    @pytest.mark.run(order=1)
    def test_AAHHeadingDisplays(self):
        self.gp.clickGameplaySideNav()
        result = self.gp.verifyAAHHeadingDisplays()
        self.ts.markFinal("test_AAHHeadingDisplays", result, "Abandon All Hope Label Displays")

    # #Verify Flavor Text Displays

    @pytest.mark.run(order=2)
    def test_FlavorTextDisplays(self):
        self.gp.clickGameplaySideNav()
        result = self.gp.verifyGameplayFlavorTextDisplays()
        self.ts.markFinal("test_FlavorTextDisplays", result, "Gameplay Flavor Text Displays")

    #Verify GamePlay Video Displays

    @pytest.mark.run(order=3)
    def test_GameplayVideoDisplays(self):
        self.gp.clickGameplaySideNav()
        time.sleep(2)
        self.gp.clickGameplayPlayIcon()
        time.sleep(5)
        result = self.gp.verifyGameplayIconVideo()
        self.ts.markFinal("test_GameplayVideoDisplays", result, "Gameplay Video Displays")
