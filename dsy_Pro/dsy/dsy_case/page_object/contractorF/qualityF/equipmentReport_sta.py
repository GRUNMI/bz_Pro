import time
import unittest

from dsy.dsy_case.page_object.contractorF.qualityF.equipment.equipmentReportPage import equipment
from dsy.dsy_case.common.myunit import MyTest
from dsy.dsy_case.common.screenshot import screen_image
from dsy.dsy_case.page_object.loginPage import LoginPage


class newEquipmentTest(MyTest):
    '''设备报审'''
    def equipment_verify(self):
        LoginPage(self.driver).login('13733333333', '88888888')
        equipment(self.driver).new_equipment()

    def test_newBrand1(self):
        '''设备报审'''
        self.equipment_verify()
        time.sleep(1)
        screen_image(self.driver, '设备报审')


if __name__ == '__main__':
    unittest.main()
