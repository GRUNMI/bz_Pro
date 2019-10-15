import unittest
from .mydriver import browser


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
