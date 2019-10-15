import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.rawMaterial.brandReportPage import Brand
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class BrandReportTest(MyTest):
    '''品牌报审'''
    def brand_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        Brand(self.driver).mainBrandReport()

    def test_BrandReport1(self):
        '''品牌报审'''
        self.brand_verify()
        time.sleep(1)
        screen_image(self.driver, '品牌报审')


if __name__ == '__main__':
    unittest.main()
