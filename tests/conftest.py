# File used to organize FIXTURES, PLUGINS, CONFIGURATIONS, etc.

import pytest
import utils.general

@pytest.fixture()
def driver():
    driver = utils.general.start_browser('headless')
    utils.general.start_app(driver)
    yield driver
    utils.general.close_browser(driver)