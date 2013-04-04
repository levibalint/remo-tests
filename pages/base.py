#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page, PageRegion


class Base(Page):

    @property
    def header(self):
        return self.Header(self.testsetup)

    class Header(Page):

        _main_menu_locator = (By.CSS_SELECTOR, '#navigation-box > ul.nav-bar > li > a')
        _events_locator = (By.CSS_SELECTOR, '#navigation-box li:nth-child(3) a')
        _labs_locator = (By.CSS_SELECTOR, '#navigation-box li:nth-child(6) a')

        @property
        def main_menu(self):
            return [self.MainMenu(self.testsetup, item) for item in self.find_elements(*self._main_menu_locator)]

        def click_events_link(self):
            self.selenium.find_element(*self._events_locator).click()
            from pages.events import Events
            return Events(self.testsetup)

        @property
        def click_labs_link(self):
            self.selenium.find_element(*self._labs_locator).click()
            from pages.labs import Labs
            return Labs(self.testsetup)

        class MainMenu(PageRegion):

            @property
            def text(self):
                return self._root_element.text

            def click(self):
                self._root_element.click()
