from django.test import LiveServerTestCase
from selenium import webdriver

class ContactsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Contacts', body.text)
