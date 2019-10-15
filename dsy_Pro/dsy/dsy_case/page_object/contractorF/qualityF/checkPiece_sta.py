import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.testPiece.checkBlockPage import briquette
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class newBriquetteTest(MyTest):
    '''试块送检'''
    def briquette_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        briquette(self.driver).new_briquette()

    def test_newBriquette1(self):
        '''试块送检'''
        self.briquette_verify()
        time.sleep(1)
        screen_image(self.driver, '试块送检')


if __name__ == '__main__':
    unittest.main()
