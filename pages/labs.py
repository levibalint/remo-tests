__author__ = 'lbalint'

from selenium.webdriver.common.by import By
from pages.base import  Base

class Labs(Base):

    _logo_locator = (By.ID, 'logo-box')