import pytest
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from flask import Flask

# class TestSelenium:
#
#     def test_it_works(self):
#         driver = webdriver.Firefox()
#         driver.get("http://www.python.org")
#         assert "Python" in driver.title
#         elem = driver.find_element_by_name("q")
#         elem.clear()
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#         driver.close()

class TestUserTakesTheTest(LiveServerTestCase):

    def create_app(self):
        # fbapp = Flask(__name__)
        #
        # # Config options - Make sure you created a 'config.py' file.
        fbapp = Flask(__name__)

        fbapp.config.from_object('config')
        return fbapp

    # def setUp(self):
    #     """Setup the test driver and create test users"""
    #     self.driver = webdriver.Firefox()
    #     self.driver.get(self.get_server_url())
    #
    #     db.session.commit()
    #     db.drop_all()
    #     db.create_all()
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_server_is_up_and_running(self):
        driver = webdriver.Firefox()
        response = driver.get(self.get_server_url())
        self.assertEqual(response.code, 200)
    #
    # def test_user_navigation(self):
    #     DRIVER.get('/')
    #     assert "Le test ultime !" in DRIVER.title
