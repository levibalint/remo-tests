 #!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.home import Home

from pages.link_crawler import LinkCrawler

class TestLabs:

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_labs_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/labs', {'class': 'twelve columns'})
        bad_urls = []

        Assert.greater(len(urls), 0, u'something went wrong. no links found.')

        for url in urls:
            print url
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            u'%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
