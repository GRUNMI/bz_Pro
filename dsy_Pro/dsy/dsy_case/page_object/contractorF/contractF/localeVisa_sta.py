import time
import unittest

from dsy.dsy_case.page_object.contractorF.contractF.projectChangeF.localeVisaPage import localeVisa
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class localeVisaTest(MyTest):
    '''现场签证'''
    def localeVisa_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        localeVisa(self.driver).mainLocaleVisa()

    def test_localeChange1(self):
        '''现场签证'''
        self.localeVisa_verify()
        time.sleep(2)
        screen_image(self.driver, '现场签证')


if __name__ == '__main__':
    unittest.main()
