import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.rawMaterial.materialReportPage import materials
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class newMaterialsTest(MyTest):
    '''材料报审'''
    def Materials_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        materials(self.driver).new_mayerials()

    def test_newMaterials1(self):
        '''材料报审'''
        self.Materials_verify()
        time.sleep(1)
        screen_image(self.driver, '材料报审')


if __name__ == '__main__':
    unittest.main()
