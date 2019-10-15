import unittest
from .projectChangeZ.localeChangePageF import localeChangeF
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.page_object.loginPage import LoginPage
from dsy.dsy_case.common.screenshot import screen_image
import time
from dsy.dsy_case.common.config import myconfig
class localeChangeFTest(MyTest):
    '''分包现场变更'''
    def localeChangeF_verify(self):
        LoginPage(self.driver).login(username=myconfig().sgZuser(), pwd=myconfig().sgZpwd())
        localeChangeF(self.driver).mainLocaleChangeF()

    def test_localeChangeF1(self):
        '''办理分包现场变更'''
        self.localeChangeF_verify()
        time.sleep(2)
        screen_image(self.driver, "分包现场变更")

if __name__ == '__main__':
        unittest.main()
