from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.world.world_page import WorldPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/world_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestWorld(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.wp = WorldPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Explore Sanctuary Heading Displays
    @pytest.mark.run(order=1)
    def test_ESHeadingDisplays(self):
        self.wp.clickWorldSideNav()
        result = self.wp.verifyESHeadingDisplays()
        self.ts.markFinal("test_ESHeadingDisplays", result, "Explore Sanctuary Heading Displays")

    # Verify World Flavor Text Displays
    @pytest.mark.run(order=2)
    def test_WorldFlavorTextDisplays(self):
        self.wp.clickWorldSideNav()
        result = self.wp.verifyWorldFlavorTextDisplays()
        self.ts.markFinal("test_WorldFlavorTextDisplays", result, "World Flavor Text Displays")

    #Verify Behold The World Icon Displays
    @pytest.mark.run(order=3)
    def test_BeholdTheWorldIconDisplays(self):
        self.wp.clickWorldSideNav()
        result = self.wp.verifyBTWIconDisplays()
        self.ts.markFinal("test_BeholdTheWorldIconDisplays", result, "Behold The World Icon Displays")

