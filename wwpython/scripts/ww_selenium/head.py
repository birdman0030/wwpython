#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class Head(SeleniumWrapper):
    TITLE = (By.CSS_SELECTOR, "head > title")

    logger = logging.getLogger("head")

    def __init__(self, driver):
        super().__init__(driver)

    def getHeaderTitleText(self):
        element_text = self.getElementText(self.TITLE)
        return element_text
