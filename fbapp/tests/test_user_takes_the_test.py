from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from flask import url_for

from .. import app
from .. import models

class TestUserTakesTheTest(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('fbapp.tests.config')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Firefox()
        self.result_page = url_for('result',
                           first_name=app.config['FB_FIRST_NAME'],
                           id=app.config['FB_USER_ID'],
                           gender=app.config['FB_USER_GENDER'],
                           _external=True)
        models.init_db(app.config['ADMIN_EMAIL'], app.config['ADMIN_PW'])
        self.wait = ui.WebDriverWait(self.driver, 1000)

    def tearDown(self):
        self.driver.quit()

    def get_el(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def enter_text_field(self, selector, text):
        text_field = self.get_el(selector)
        text_field.clear()
        text_field.send_keys(text)

    def clicks_on_login(self):
        button = self.get_el(".fb-login-button")
        self.wait.until(lambda driver: self.driver.find_element_by_tag_name("iframe").is_displayed())
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
        self.wait.until(lambda driver: len(self.driver.window_handles) == 1)
        # Wait for the redirection to be completed
        self.wait.until(lambda driver: '?' in self.driver.current_url)
        self.wait.until(lambda driver: 'aaa' in self.driver.current_url)
        assert self.driver.current_url == self.result_page

    def test_result_page_name(self):
        self.driver.get(self.result_page)
        assert self.get_el('#user_name').text == app.config['FB_FIRST_NAME'].upper()

    def test_result_page_description(self):
        # Check that the shown description matches our user.
        self.driver.get(self.result_page)
        shown_desc = self.get_el('#description').text
        db_desc = models.Content.query.filter(models.Content.description == shown_desc).all()
        # import pdb; pdb.set_trace()
        assert db_desc[0].gender == models.Genders[app.config['FB_USER_GENDER']]

    def test_result_page_img(self):
        # Check that an image is displayed for this user
        self.driver.get(self.result_page)
        img = self.get_el('#user_image').get_attribute('src')
        assert app.config['FB_USER_ID'] in img
