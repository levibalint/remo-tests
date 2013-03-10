__author__ = 'lbalint'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base import  Base


class Events(Base):

    _search_locator = (By.ID, "searchfield")
    _loading_wrapper_locator = (By.ID, "events-loading-wrapper")
    _event_item_locator = (By.CSS_SELECTOR, '.event-item')

    @property
    def is_search_visible(self):
        return self.is_element_visible(*self._search_locator)

    def search_for(self, value):
        self.type_in_element(self._search_locator, value)

    def wait_for_wrapper_not_visible (self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._loading_wrapper_locator))

    @property
    def events_number(self):
        return len(self.selenium.find_elements(*self._event_item_locator))