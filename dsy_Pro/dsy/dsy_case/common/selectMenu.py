'''
选择菜单
'''
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dsy.dsy_case.common.base import Base


class Menu(Base):
    def submenu(self, menu_ele, submenu_ele):
        # 等待菜单按钮出来
        if WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(menu_ele)):
            '''选择菜单'''
            ActionChains(self.driver).move_to_element(self.find_element(*menu_ele)).perform()
            self.find_element(*submenu_ele).click()
            time.sleep(1)
        else:
            self.driver.quit()
