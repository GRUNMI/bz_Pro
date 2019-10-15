import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu

'''
试件送检
'''
class block(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    submenu_ele = (By.LINK_TEXT, "试块试件")
    block_report_ele = (By.LINK_TEXT, "试件送检")
    new_block_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/form/div[3]/span/a")
    date_ele = (By.CSS_SELECTOR, '.form-control.pointer')
    unit_project_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[2]/div/select")
    partAddSortAddStandard_ele = (By.CSS_SELECTOR, '.form-control.w-300')   # 试件部位、试件种类、试件规格
    specification_ele = (By.CSS_SELECTOR, '.form-control.left.w-300')  # 试件规格
    select_person_ele = (By.LINK_TEXT, "选择人")
    select_company_ele = (By.XPATH, "html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/h3")
    # 刘馨儿（哈工大施工总包二工程-项目管理员）
    select_person_name_ele = (
    By.XPATH, "html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/ul/li[1]/h3/span")
    confirm_select_ele = (By.LINK_TEXT, "选择")
    active_select_ele = (By.CSS_SELECTOR, '.btn.btn-warning')
    active_ele = (By.LINK_TEXT, "提交")
    active_new_ele = (By.LINK_TEXT, "提交并新增")
    draft_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[7]/div/button[3]")  # 草稿

    def select_menu(self):
        Menu(self.driver).submenu(menu_ele=self.menu_ele, submenu_ele=self.submenu_ele)

    def select_module(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.block_report_ele)).click()

    def click_new(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.new_block_ele)).click()

    def input_date(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.date_ele)).click()
        self.find_element(By.CSS_SELECTOR, '.day.active').click()
        # self.remove_date_readonly(css_selector='.form-control.pointer')
        # js_value = 'document.querySelector(".form-control.pointer").value="2017-10-08"'
        # self.driver.execute_script(js_value)
        # self.find_element(*self.date_ele).send_keys(date)

    def select_unit_project(self):
        Select(self.find_element(*self.unit_project_ele)).select_by_visible_text("20170913群楼层12(裙楼层)")

    def input_partAddSortAddStandard(self, part, sort, standard):
        values = [part, sort, standard]
        index = 0
        partAddSortAddStandard = self.find_elements(*self.partAddSortAddStandard_ele)
        for ele in partAddSortAddStandard:
            ele.send_keys(values[index])
            index += 1

    def click_select_person(self):
        self.find_element(*self.select_person_ele).click()

    def click_company(self):
        self.find_element(*self.select_company_ele).click()

    def click_preson_name(self):
        self.find_element(*self.select_person_name_ele).click()

    def confirm_select(self):
        self.find_element(*self.confirm_select_ele).click()

    def active_select(self):
        self.find_element(*self.active_select_ele).click()

    def active(self):
        self.find_element(*self.active_ele).click()

    def active_new(self):
        self.find_element(*self.active_new_ele).click()

    def draft(self):
        self.find_element(*self.draft_ele).click()

    def new_block(self):
        self.select_menu()
        self.select_module()
        self.click_new()
        # self.input_date()
        self.select_unit_project()
        self.input_partAddSortAddStandard("部位", "种类", "规格")
        self.click_select_person()
        self.click_company()
        self.click_preson_name()
        self.confirm_select()
        self.active_select()
        self.input_date()
        self.draft()
