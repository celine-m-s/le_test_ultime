import pytest
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

from flask import Flask

from .. import app
from .. import models

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
        app.config.from_object('fbapp.tests.testing')
        app.config.debug = True
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Firefox()
        self.result_page = self.get_server_url() + '/result?first_name=Tom&id=111823112767411&gender=male'
        models.init_db(app.config['ADMIN_EMAIL'], app.config['ADMIN_PW'])
        self.wait = ui.WebDriverWait(self.driver,1000)

    def tearDown(self):
        self.driver.quit()

    # def test_server_is_up_and_running(self):
    #     import urllib.request
    #     response = urllib.request.urlopen(self.get_server_url())
    #     self.assertEqual(response.code, 200)
    #
    # def test_title_navigation(self):
    #     self.driver.get(self.get_server_url())
    #     assert "Le test ultime !" in self.driver.title

    def get_el(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def enter_text_field(self, selector, text):
        text_field = self.get_el(selector)
        text_field.clear()
        text_field.send_keys(text)

    def clicks_on_login(self):
        button = self.get_el(".fb-login-button")
        # Wait for FB to be initialized
        # import pdb; pdb.set_trace()
        self.wait.until(lambda driver: self.driver.find_element_by_tag_name("iframe").is_displayed())
        # import pdb; pdb.set_trace()
        ActionChains(self.driver).click(button).perform()

    def sees_login_page(self):
        # Wait for the second window to appear
        self.wait.until(lambda driver: len(self.driver.window_handles) > 1)
        # Switch windows to go on the Login page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Wait for the page to be loaded
        self.wait.until(lambda driver: self.get_el('#email'))
        assert self.driver.current_url.startswith('https://www.facebook.com/login.php') # <3 Python

    def submits_form(self):
        self.enter_text_field('#email', app.config['FB_EMAIL'])
        self.enter_text_field('#pass', app.config['FB_PASSWORD'])
        self.get_el('#loginbutton input[name=login]').click()


    def test_user_login(self):
        self.driver.get(self.get_server_url())
        self.clicks_on_login()
        self.sees_login_page()
        self.submits_form()
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Wait for the FB login page to be closed.
        self.wait.until(lambda driver: len(self.driver.window_handles) == 1) # OK
        # Wait for the redirection to be completed
        self.wait.until(lambda driver: len(self.driver.current_url) > len(self.get_server_url())+1)
        assert self.driver.current_url == self.result_page

    def test_result_page_name(self):
        self.driver.get(self.result_page)
        assert self.get_el('#user_name').text == app.config['FB_FIRST_NAME'].upper()

    def test_result_page_description(self):
        # Check that the shown description matches our user.
        self.driver.get(self.result_page)
        shown_desc = self.get_el('#description').text
        db_desc = models.Content.query.filter(models.Content.description == shown_desc).all()
        assert db_desc[0].gender == 'male'

    def test_result_page_img(self):
        # Check that an image is displayed for this user
        self.driver.get(self.result_page)
        img = self.get_el('#user_image').get_attribute('src')
        assert '111823112767411' in img
