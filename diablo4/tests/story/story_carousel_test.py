from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.story.story_carousel_page import StoryCarouselPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

# Run this page -  pytest -s -v tests/common/story_carousel_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestStoryCarousel(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.scp = StoryCarouselPage(self.driver)
        self.ts = TestStatus(self.driver)


    #Verify Story Slide Left Arrow 1 Displays

    #@pytest.mark.run(order=#)
    def test_SlideLeftArrow1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifySlideLeftArrow1Displays()
        self.ts.markFinal("test_SlideLeftArrow1Displays", result, "Story Slide Left Arrow 1 Displays")

    #Verify Story Slide Right Arrow 1 Displays

    #@pytest.mark.run(order=#)
    def test_SlideRightArrow1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifySlideRightArrow1Displays()
        self.ts.markFinal("test_SlideRightArrow1Displays", result, "Story Slide Right Arrow 1 Displays")

    #Verify Story Slide Left Arrow 2 Displays

    # @pytest.mark.run(order=#)
    def test_SlideLeftArrow2Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton2()
        result = self.scp.verifySlideLeftArrow2Displays()
        self.ts.markFinal("test_SlideLeftArrow2Displays", result, "Story Slide Left Arrow 2 Displays")

    #Verify Story Slide Right Arrow 2 Displays

    # @pytest.mark.run(order=#)
    def test_SlideRightArrow2Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton2()
        result = self.scp.verifySlideRightArrow2Displays()
        self.ts.markFinal("test_SlideRightArrow2Displays", result, "Story Slide Right Arrow 2 Displays")

    #Verify Story Slide Left Arrow 3 Displays

    #@pytest.mark.run(order=#)
    def test_SlideLeftArrow3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifySlideLeftArrow3Displays()
        self.ts.markFinal("test_SlideLeftArrow3Displays", result, "Story Slide Left Arrow 3 Displays")

    #Verify Story Slide Right Arrow 3 Displays

    #@pytest.mark.run(order=#)
    def test_SlideRightArrow3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifySlideRightArrow3Displays()
        self.ts.markFinal("test_SlideRightArrow3Displays", result, "Story Slide Right Arrow 3 Displays")

    #Verify Story Slide Left Arrow 4 Displays

    # @pytest.mark.run(order=#)
    def test_SlideLeftArrow4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifySlideLeftArrow4Displays()
        self.ts.markFinal("test_SlideLeftArrow4Displays", result, "Story Slide Left Arrow 4 Displays")

    #Verify Story Slide Right Arrow 4 Displays

    # @pytest.mark.run(order=#)
    def test_SlideRightArrow4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifySlideRightArrow4Displays()
        self.ts.markFinal("test_SlideRightArrow4Displays", result, "Story Slide Right Arrow 4 Displays")

    #Verify Story Slide Left Arrow 5 Displays

    # @pytest.mark.run(order=#)
    def test_SlideLeftArrow5Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton5()
        result = self.scp.verifySlideLeftArrow5Displays()
        self.ts.markFinal("test_SlideLeftArrow5Displays", result, "Story Slide Left Arrow 5 Displays")

    #Verify Story Slide Right Arrow 5 Displays

    # @pytest.mark.run(order=#)
    def test_SlideRightArrow5Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton5()
        result = self.scp.verifySlideRightArrow5Displays()
        self.ts.markFinal("test_SlideRightArrow5Displays", result, "Story Slide Right Arrow 5 Displays")

    #Verify Story Slide Image 1 Displays

    #@pytest.mark.run(order=#)

    def test_SlideImage1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifyStorySlideImage1Displays()
        self.ts.markFinal("test_SlideImage1Displays", result, "Story Slide Image 1 Displays")

    #Verify Story Slide Image 2 Displays

    # @pytest.mark.run(order=#)

    def test_SlideImage2Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton2()
        result = self.scp.verifyStorySlideImage2Displays()
        self.ts.markFinal("test_SlideImage2Displays", result, "Story Slide Image 2 Displays")

    # Verify Story Slide Image 3 Displays

    # @pytest.mark.run(order=#)

    def test_SlideImage3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifyStorySlideImage3Displays()
        self.ts.markFinal("test_SlideImage3Displays", result, "Story Slide Image 3 Displays")

    # Verify Story Slide Image 4 Displays

    # @pytest.mark.run(order=#)

    def test_SlideImage4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifyStorySlideImage4Displays()
        self.ts.markFinal("test_SlideImage4Displays", result, "Story Slide Image 4 Displays")

    # Verify Story Slide Image 5 Displays

    # @pytest.mark.run(order=#)

    def test_SlideImage5Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton5()
        result = self.scp.verifyStorySlideImage5Displays()
        self.ts.markFinal("test_SlideImage5Displays", result, "Story Slide Image 5 Displays")

    # Verify Story Slide Button 1 Displays

    # @pytest.mark.run(order=#)

    def test_StorySlideButton1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifyStorySlideButton1Displays()
        self.ts.markFinal("test_StorySlideButton1Displays", result, "Story Slide Button 1 Displays")

    #Verify Story Slide Button 2 Displays

    # @pytest.mark.run(order=#)

    def test_StorySlideButton2Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton2()
        result = self.scp.verifyStorySlideButton2Displays()
        self.ts.markFinal("test_StorySlideButton2Displays", result, "Story Slide Button 2 Displays")

    # Verify Story Slide Button 3 Displays

    # @pytest.mark.run(order=#)

    def test_StorySlideButton3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifyStorySlideButton3Displays()
        self.ts.markFinal("test_StorySlideButton3Displays", result, "Story Slide Button 3 Displays")

    # Verify Story Slide Button 4 Displays

    # @pytest.mark.run(order=#)

    def test_StorySlideButton4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifyStorySlideButton4Displays()
        self.ts.markFinal("test_StorySlideButton4Displays", result, "Story Slide Button 4 Displays")

    # Verify Story Slide Button 5 Displays

    # @pytest.mark.run(order=#)

    def test_StorySlideButton5Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton5()
        result = self.scp.verifyStorySlideButton5Displays()
        self.ts.markFinal("test_StorySlideButton5Displays", result, "Story Slide Button 5 Displays")

    # Verify Story Heading 1 Displays

    # @pytest.mark.run(order=#)

    def test_StoryHeading1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifyStoryHeading1Displays()
        self.ts.markFinal("test_StoryHeading1Displays", result, "Story Heading 1 Displays")

    # Verify Story Heading 2 Displays

    # @pytest.mark.run(order=#)

    def test_StoryHeading2Displays(self):
            self.scp.clickStorySideNav()
            self.scp.clickStoryCrossIcon()
            self.scp.clickSlideButton2()
            result = self.scp.verifyStoryHeading2Displays()
            self.ts.markFinal("test_StoryHeading2Displays", result, "Story Heading 2 Displays")

    # Verify Story Heading 3 Displays

    # @pytest.mark.run(order=#)

    def test_StoryHeading3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifyStoryHeading3Displays()
        self.ts.markFinal("test_StoryHeading3Displays", result, "Story Heading 3 Displays")

    # Verify Story Heading 4 Displays

    # @pytest.mark.run(order=#)

    def test_StoryHeading4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifyStoryHeading4Displays()
        self.ts.markFinal("test_StoryHeading4Displays", result, "Story Heading 4 Displays")

    # Verify Story Heading 5 Displays

    # @pytest.mark.run(order=#)

    def test_StoryHeading5Displays(self):
            self.scp.clickStorySideNav()
            self.scp.clickStoryCrossIcon()
            self.scp.clickSlideButton5()
            result = self.scp.verifyStoryHeading5Displays()
            self.ts.markFinal("test_StoryHeading5Displays", result, "Story Heading 5 Displays")

    # Verify Story Paragraph 1 Displays

    # @pytest.mark.run(order=#)

    def test_StoryParagraph1Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifyStoryParagraph1Displays()
        self.ts.markFinal("test_StoryParagraph1Displays", result, "Story Paragraph 1 Displays")

    # Verify Story Paragraph 2 Displays

    # @pytest.mark.run(order=#)

    def test_StoryParagraph2Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton2()
        result = self.scp.verifyStoryParagraph2Displays()
        self.ts.markFinal("test_StoryParagraph2Displays", result, "Story Paragraph 2 Displays")

    # Verify Story Paragraph 3 Displays

    # @pytest.mark.run(order=#)

    def test_StoryParagraph3Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton3()
        result = self.scp.verifyStoryParagraph3Displays()
        self.ts.markFinal("test_StoryParagraph3Displays", result, "Story Paragraph 3 Displays")

    # Verify Story Paragraph 4 Displays

    # @pytest.mark.run(order=#)

    def test_StoryParagraph4Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton4()
        result = self.scp.verifyStoryParagraph4Displays()
        self.ts.markFinal("test_StoryParagraph4Displays", result, "Story Paragraph 4 Displays")

    # Verify Story Paragraph 5 Displays

    # @pytest.mark.run(order=#)

    def test_StoryParagraph5Displays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton5()
        result = self.scp.verifyStoryParagraph5Displays()
        self.ts.markFinal("test_StoryParagraph5Displays", result, "Story Paragraph 5 Displays")

    # Verify Story Slide X Icon Displays

    # @pytest.mark.run(order=#)
    def test_SlideXIconDisplays(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        result = self.scp.verifySlideStoryXDisplays()
        self.ts.markFinal("test_SlideXIconDisplays", result, "Story Slide X Closing Icon Displays")

    # Verify Story Slide X Icon Closes & Displays Story Section

    # @pytest.mark.run(order=#)
    def test_SlideXIconCloses(self):
        self.scp.clickStorySideNav()
        self.scp.clickStoryCrossIcon()
        self.scp.clickSlideButton1()
        self.scp.clickStoryXClose()
        result = self.scp.verifyStorySideNavDisplays()
        self.ts.markFinal("test_SlideXIconCloses", result, "Story Slide X Closes Slide")


















