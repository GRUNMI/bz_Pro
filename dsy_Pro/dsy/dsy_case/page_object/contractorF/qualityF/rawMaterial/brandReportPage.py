import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu

'''
品牌报审
'''
class Brand(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    subMenu_ele = (By.LINK_TEXT, "设备")
    brand_ele = (By.LINK_TEXT, "品牌报审")
    brandReport_ele = (By.CSS_SELECTOR, '.right.btn.btn-warning')

    tabels_ele = (By.CSS_SELECTOR, '.w_90.form-control.border1')  # 5个输入框
    activeButton_ele = (By.CSS_SELECTOR, '.btn.btn-active')  # 提交
    draft_ele = (By.LINK_TEXT, "存草稿")
    close_ele = (By.LINK_TEXT, "关闭")

    def selectMenu(self):
        Menu(self.driver).submenu(menu_ele=self.menu_ele, submenu_ele=self.subMenu_ele)

    def selectBrand(self):
        self.find_element(*self.brand_ele).click()

    def brandReport(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.brandReport_ele)).click()


    def fillInTabel(self, name, brand, model='', manufacturer='', remark=''):
        '''

        :param name: 设备名称
        :param brand:品牌
        :param model:规格型号
        :param manufacturer:厂商
        :param remark:备注
        :return:
        '''
        current_handle = self.driver.current_window_handle
        # print(current_handle)
        all_handler = self.driver.window_handles
        # print(all_handler)
        for handle in all_handler:
            if handle != current_handle:
                # print(handle)
                self.driver.switch_to_window(handle)
                # print(self.driver.window_handles)
                tables = self.find_elements(*self.tabels_ele)
                contexts = [name, brand, model, manufacturer, remark]
                index = 0
                for table in tables:
                    table.send_keys(contexts[index])
                    index += 1
            else:
                continue


    def click_active(self):
        self.scroll_go_to_ele(*self.activeButton_ele)
        self.find_element(*self.activeButton_ele).click()

    def click_draft(self):
        self.scroll_go_to_ele(*self.draft_ele)
        self.find_element(*self.draft_ele).click()

    def click_close(self):
        self.scroll_go_to_ele(*self.close_ele)
        self.find_element(*self.close_ele).click()

    def mainBrandReport(self):
        self.selectMenu()
        self.selectBrand()
        self.brandReport()
        self.fillInTabel(1, 2)
        time.sleep(5)

