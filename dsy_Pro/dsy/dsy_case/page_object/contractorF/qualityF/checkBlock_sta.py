import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.testPiece.checkPiecePage import block
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class newblockTest(MyTest):
    '''试件送检'''
    def block_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        block(self.driver).new_block()

    def test_newblock1(self):
        '''试件送检'''
        self.block_verify()
        time.sleep(1)
        screen_image(self.driver, '试件送检')


if __name__ == '__main__':
    unittest.main()
