import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.checkBatch.checkPutPage import checkPut
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class checkPutTest(MyTest):
    '''检验批实施'''
    def checkPut_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        checkPut(self.driver).mainCkectPut()

    def test_CheckPut1(self):
        '''检验批实施'''
        self.checkPut_verify()
        time.sleep(1)
        screen_image(self.driver, '检验批实施')


if __name__ == '__main__':
    unittest.main()