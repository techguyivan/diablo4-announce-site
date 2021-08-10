from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.story.story_page import StoryPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/story_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestStory(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.sp = StoryPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Meet Your Maker Heading Displays
    @pytest.mark.run(order=1)
    def test_MYMHeadingDisplays(self):
        self.sp.clickStorySideNav()
        result = self.sp.verifyMYMHeadingDisplays()
        self.ts.markFinal("test_MYMHeadingDisplays", result, "Meet Your Maker Heading Displays")

    #Verify Meet Your Maker Sub Heading Displays
    @pytest.mark.run(order=2)
    def test_MYMSubHeadingDisplays(self):
        self.sp.clickStorySideNav()
        result = self.sp.verifyMYMSubHeadingDisplays()
        self.ts.markFinal("test_MYMSubHeadingDisplays", result, "Meet Your Maker Sub Heading Displays")

    #Verify Story Cross Icon Displays
    @pytest.mark.run(order=3)
    def test_SCIDisplays(self):
        self.sp.clickStorySideNav()
        result = self.sp.verifyStoryCrossIconDisplays()
        self.ts.markFinal("test_SCIDisplays", result, "Story Cross Icon Displays")