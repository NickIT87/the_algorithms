import unittest
import time
from selenium import webdriver


class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        capabilities = {
            "browserName": "chrome",
            "version": "77.0",
            "enableVNC": True,
            "enableVideo": False
        }
        self.driver = webdriver.Remote(
            command_executor="http://192.168.0.105:4444/wd/hub",
            desired_capabilities=capabilities)
        #navigate to the application home page
        self.driver.get("http://www.google.com")

    def test_search_by_category(self):
        self.search_input = self.driver.find_element_by_name("q")
        self.search_input.send_keys("test")
        self.search_input.submit()
        #time.sleep(5)

    def tearDown(self):
        time.sleep(5)
        #close the session
        #self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)