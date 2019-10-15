import time
from selenium.webdriver.common.by import By
from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
现场签证
'''
class localeVisa(Base):
    Menu_ele = (By.LINK_TEXT, "合同管理")
    subMenu_ele = (By.LINK_TEXT, "工程变更")
    localeChange_ele = (By.LINK_TEXT, "现场签证")
    launchChange_ele = (By.CSS_SELECTOR, '.mr-10.btn.btn-warning')
    # table
    reason_ele = (By.CSS_SELECTOR, '.from-text.b-bt.w-550')
    message_ele = (By.ID, 'comment')
    active_ele = (By.CSS_SELECTOR, '.btn.btn-active')  # 提交
    saveDraft_ele = (By.XPATH, "//*[@id='appBody']/div[3]/div[2]/div[2]/div[2]/button")  # 草稿
    close_ele = (By.XPATH, "//*[@id='appBody']/div[3]/div[2]/div[2]/div[3]/button")  # 关闭
    confirm_ele = (By.CSS_SELECTOR, '.btn.btn-warning')
    saveSucceed_ele = (By.CSS_SELECTOR, '.btn.btn-warning.btn-alert')

    def selectMenu(self):
        Menu(self.driver).submenu(menu_ele=self.Menu_ele, submenu_ele=self.subMenu_ele)

    def selectLocaleChange(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.localeChange_ele)).click()

    def change(self):
        change = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.launchChange_ele))
        time.sleep(1)
        change.click()

    def fillInTable(self):
        time.sleep(1)
        all_handlers = self.driver.window_handles
        print(all_handlers)
        self.driver.switch_to.window(all_handlers[-1])
        print(self.driver.current_window_handle)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.reason_ele)).send_keys("reason")
        self.scroll_bottom()
        self.find_element(*self.message_ele).send_keys("message")

    def saveDraft(self):
        self.find_element(*self.saveDraft_ele).click()
        self.find_element(*self.confirm_ele).click()

    def saveSucceed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.saveSucceed_ele)).click()

    def backList(self):
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[0])
        print(self.driver.current_window_handle)

    def mainLocaleVisa(self):
        self.selectMenu()
        self.selectLocaleChange()
        self.change()
        self.fillInTable()
        self.saveDraft()
        self.saveSucceed()
        self.backList()
