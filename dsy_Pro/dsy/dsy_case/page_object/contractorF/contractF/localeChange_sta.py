import time
import unittest

from dsy.dsy_case.page_object.contractorF.contractF.projectChangeF.localeChangePage import localeChange
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class localeChangeTest(MyTest):
    '''现场变更'''
    def localeChange_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        localeChange(self.driver).mainLocaleChange()

    def test_localeChange1(self):
        '''现场变更'''
        self.localeChange_verify()
        time.sleep(2)
        screen_image(self.driver, '现场变更')


if __name__ == '__main__':
    unittest.main()
