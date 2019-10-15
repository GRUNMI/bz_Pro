import time
from selenium.webdriver.common.by import By
from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



'''
分包现场变更
'''

class localeChangeF(Base):
    menu_ele = (By.LINK_TEXT, "合同管理")
    subMenu_ele = (By.LINK_TEXT, "工程变更")
    localeChange_ele = (By.LINK_TEXT, "现场变更")
    localeChangeF_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[1]/div[2]/div/a[2]")
    transactFile_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/div[2]/table/tbody/tr[1]/td[16]/span/span[1]/a")
    # table
    message_ele = (By.ID, 'comment')
    close_ele = (By.XPATH, "//*[@id='appBody']/div[3]/div[2]/div[3]/div[4]/button")

    def selectMenu(self):
        Menu(self.driver).submenu(menu_ele=self.menu_ele, submenu_ele=self.subMenu_ele)

    def selectLocaleChange(self):
        LocaleChange = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.localeChange_ele))
        time.sleep(1)
        LocaleChange.click()

    def selectLocaleChangeF(self):
        time.sleep(1)
        LocaleChangeF = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.localeChangeF_ele))
        time.sleep(1)
        LocaleChangeF.click()

    def transactFile(self):
        transactButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.transactFile_ele))
        time.sleep(1)
        transactButton.click()

    def fillInTable(self):
        time.sleep(1)
        all_handle = self.driver.window_handles
        # print(all_handle)
        self.driver.switch_to.window(all_handle[-1])
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.message_ele))
        self.scroll_bottom()
        message.send_keys("message")

    def mainLocaleChangeF(self):
        self.selectMenu()
        self.selectLocaleChange()
        self.selectLocaleChangeF()
        self.transactFile()
        self.fillInTable()
