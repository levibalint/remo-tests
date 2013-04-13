#!/usr/bin/env python

import pytest
import time

from pages.home import Home
from unittestzero import Assert

class TestSearchDemo:

    @pytest.mark.nondestructive
    def test_search(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()

        home.header.click_events_link()
        events = home.header.click_events_link()

        Assert.true(events.is_search_visible)

        events.search_for('test')

        time.sleep(15)

        Assert.equal(events.events_number, 1)
