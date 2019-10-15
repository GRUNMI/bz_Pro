import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu

'''
检验批实施
'''
class checkPut(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    subMenu_ele = (By.LINK_TEXT, "检验批/分项管理")
    checkPut_ele = (By.LINK_TEXT, "检验批实施")
    checkReport_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/div/div[2]/table/tbody/tr/td[3]/a[4]/span")
    applyForCheck_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/div[2]/form/div[7]/span/a")
    startFile_ele = (By.XPATH, ".//*[@id='appBody']/div/div/div[2]/div/table/tbody/tr[1]/td[5]/a")
    table1_ele = (By.ID, 'A5')
    draft_ele = (By.XPATH, "//*[@id='appBody']/div[3]/div[2]/div[2]/div[2]/button")  # 草稿
    confirm_ele = (By.CSS_SELECTOR, '.btn.btn-warning')
    saveSucceed_ele = (By.CSS_SELECTOR, '.btn.btn-warning.btn-alert')
    backList_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/div/form/div[3]/button[4]")

    def selectMenu(self):
        Menu(self.driver).submenu(menu_ele=self.menu_ele, submenu_ele=self.subMenu_ele)

    def selectCheckPut(self):
        WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(self.checkPut_ele)).click()

    def selectCheckReport(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.checkReport_ele)).click()
        time.sleep(1)

    def selectApplyForCheck(self):
        WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(self.applyForCheck_ele)).click()

    def selectStartFile(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.startFile_ele)).click()

    def fillInTable(self):
        # current_handle = self.driver.current_window_handle
        # print(current_handle)
        # all_handlers = self.driver.window_handles
        # print(all_handlers)
        # for handle in all_handlers:
        #     if handle != current_handle:
        #         self.driver.switch_to.window(handle)
        #         print(handle)
        #     else:
        #         continue
        all_handlers = self.driver.window_handles
        # print(all_handlers)
        self.driver.switch_to.window(all_handlers[1])
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        frame_ele = (By.XPATH, "//*[@id='appBody']/div[2]/div/iframe")
        self.switch_frame(*frame_ele)
        # self.driver.switch_to.frame(self.find_element(*frame_ele))

    def saveDraft(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.table1_ele)).send_keys('12')
        # time.sleep(2)
        self.driver.switch_to.default_content()
        self.scroll_bottom()
        self.find_element(*self.draft_ele).click()
        self.find_element(*self.confirm_ele).click()

    def saveSucceed(self):
        self.find_element(*self.saveSucceed_ele).click()
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[0])
        # print(self.driver.current_window_handle)
        # time.sleep(5)
        backList = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.backList_ele))
        time.sleep(1)
        backList.click()
        # time.sleep(5)

    def mainCkectPut(self):
        self.selectMenu()
        self.selectCheckPut()
        self.selectCheckReport()
        self.selectApplyForCheck()
        self.selectStartFile()
        self.fillInTable()
        self.saveDraft()
        self.saveSucceed()

