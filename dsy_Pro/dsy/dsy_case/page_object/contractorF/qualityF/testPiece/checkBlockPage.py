import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from dsy.dsy_case.common.base import Base
from dsy.dsy_case.common.selectMenu import Menu

'''
试块送检
'''
class briquette(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    briquette_ele = (By.LINK_TEXT, "试块试件")
    briquette_report_ele = (By.LINK_TEXT, "试块送检")
    new_briquette_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[2]/form/div[2]/span/a")
    date_ele = (By.CSS_SELECTOR, '.form-control.pointer')
    unit_project_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[2]/div/select")
    part_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[3]/div/input")
    sort_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[4]/div/select")
    way_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[5]/div/select")
    intension_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[6]/div/select")
    grade_ele = (By.XPATH, "//*[@id='appBody']/div/div/div[3]/div/form/div[7]/div/select")
    select_person_ele = (By.LINK_TEXT, "选择人")
    # select_company_ele = (By.CSS_SELECTOR, '.fs-12.lh-20.pointer.fw-300.ellipsis')
    select_company_ele = (By.XPATH, "html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/h3")
    # 刘馨儿（哈工大施工总包二工程-项目管理员）
    select_person_name_ele = (By.XPATH, "html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/ul/li[1]/h3/span")
    confirm_select_ele = (By.LINK_TEXT, "选择")
    active_select_ele = (By.CSS_SELECTOR, '.btn.btn-warning')
    active_ele = (By.LINK_TEXT, "提交")
    active_new_ele = (By.LINK_TEXT, "提交并新增")
    draft_ele = (By.LINK_TEXT, "提交")



    def select_menu(self):
        Menu(self.driver).submenu(menu_ele=self.menu_ele, submenu_ele=self.briquette_ele)

    def select_briquette_inspect(self):
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.briquette_report_ele)).click()
        # self.find_element(*self.briquette_report_ele).click()

    def click_new(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.new_briquette_ele)).click()

    def input_date(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.date_ele)).click()
        self.find_element(By.CSS_SELECTOR, '.day.active').click()
        # WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.date_ele))
        # self.remove_date_readonly(css_selector='.form-control.pointer')
        # self.remove_date_data_reactid(css_selector='.form-control.pointer')
        # self.find_element(*self.date_ele).send_keys(date)

    def select_unitProject(self, unitProject='20170913群楼层12(裙楼层)'):
        Select(self.find_element(*self.unit_project_ele)).select_by_visible_text(unitProject)

    def input_part(self, part):
        self.find_element(*self.part_ele).send_keys(part)

    def select_sort(self, sort='混凝土'):
        Select(self.find_element(*self.sort_ele)).select_by_value(sort)

    def select_way(self, way='标养'):
        Select(self.find_element(*self.way_ele)).select_by_visible_text(way)

    def select_intension(self, intension='C10'):
        Select(self.find_element(*self.intension_ele)).select_by_value(intension)

    def select_grade(self, grade='P6'):
        Select(self.find_element(*self.grade_ele)).select_by_value(grade)

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

    def new_briquette(self):
        self.select_menu()
        self.select_briquette_inspect()
        self.click_new()
        # self.input_date('2017-10-08')
        self.select_unitProject()
        self.input_part("部位")
        self.select_sort()
        self.select_way()
        # self.select_intension()  # 试块强度
        # self.select_grade()  # 试块等级
        self.click_select_person()
        self.click_company()
        self.click_preson_name()
        self.confirm_select()
        self.active_select()
        self.input_date()
