from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from dsy.dsy_case.common.base import Base

'''
材料报审
'''
class materials(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    submenu_ele = (By.LINK_TEXT, "原材料/半成品/成品/构配件")
    # frame标签
    right_iframe_ele = (By.ID, 'right_iframe')

    toolbar_ele = (By.XPATH, "//*[@id='tags']/li[5]/a")
    new_materials_ele = (By.CSS_SELECTOR, '.but-news-query.new-btn-yellow')
    date_ele = (By.ID, 'entryTime')  # 默认readonly
    materials_name_ele = (By.ID, 'name')
    standard_ele = (By.ID, 'standard')
    producer_ele = (By.ID, 'producer')
    supplier_ele = (By.ID, 'supplier')
    # select_unit_project_ele = (By.LINK_TEXT, "请选择单位工程")
    select_unit_project_ele = (By.XPATH, "//*[@id='usePlace']/div/div/select[1]")
    # select_branch_ele = (By.LINK_TEXT, "请选择分部")
    select_branch_ele = (By.XPATH, "//*[@id='usePlace']/div/div/select[2]")
    usePart_ele = (By.NAME, 'usePart')
    admissionQuantity_ele = (By.ID, 'admissionQuantity')  # 进场数量
    measurementUnits_ele = (By.ID, 'measurementUnits')  # 进场单位
    guaranteeNo_ele = (By.ID, 'guaranteeNo')
    input_warranty_ele = (
        By.XPATH,
        "//*[@id='myPageForm']/ul/li[10]/div/div/div[2]/label")  # 上传质保书
    certificateNo_ele = (By.ID, 'certificateNo')
    qualified_ele = (
        By.XPATH,
        "//*[@id='myPageForm']/ul/li[12]/div/div/div[2]/label")  # 上传合格证
    startCheckReportNo_ele = (By.ID, 'startCheckReportNo')
    startCheckReport_ele = (
        By.XPATH,
        "//*[@id='myPageForm']/ul/li[14]/div/div/div[2]/label")  # 上传出厂检测报告
    accessory_ele = (
        By.XPATH,
        "//*[@id='myPageForm']/ul/li[15]/div/div/div[2]/label")  # 上传附件
    select_inspect = (By.XPATH, ".//*[@id='myPageForm']/ul/li[16]/input[1]")
    select_No_inspect = (
        By.XPATH,
        ".//*[@id='myPageForm']/ul/li[16]/input[2]")  # 默认为否
    select_button = (By.ID, 'ZB_COMFIRM_USER')
    personList_frame_ele = (By.CSS_SELECTOR, '.layui-layer-content>iframe ')
    select_person = (By.XPATH, "//*[@id='nextorg']/li/div/dl/dd[1]/a")
    person_confirm = (By.CSS_SELECTOR, '.new-btn-yellow')
    materials_confirm = (By.CSS_SELECTOR, '.submitBtn.new-btn-yellow')
    materials_draft = (By.CSS_SELECTOR, '.submitBtn.new-btn-gray')

    def select_menu(self):
        # 等待菜单按钮出来
        if WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.menu_ele)):
            '''选择菜单'''
            ActionChains(self.driver).move_to_element(self.find_element(*self.menu_ele)).perform()
            self.find_element(*self.submenu_ele).click()
        else:
            self.driver.quit()

        # 移动光标到用户名处，使菜单栏消失
        ActionChains(self.driver).move_to_element(
            self.find_element(By.CSS_SELECTOR, '.vam.ellipsis.maxW_100.fw-700')).perform()

    def select_toolbar(self):
        self.frame_find_element(*self.right_iframe_ele)
        self.find_element(*self.toolbar_ele).click()

    def click_new(self):
        self.find_element(*self.new_materials_ele).click()

    def input_date(self, date):
        '''
        移除默认的readonly属性
        :param date: 输入时间
        :return: 选择时间
        '''
        WebDriverWait(
            self.driver, 10).until(
            EC.presence_of_element_located(
                self.date_ele))
        # js = "document.getElementById('entryTime').removeAttribute('readonly')"
        # self.driver.execute_script(js)
        self.remove_date_readonly(css_selector='#entryTime')

        self.find_element(*self.date_ele).send_keys(date)

    def input_name(self, name):
        self.find_element(*self.materials_name_ele).send_keys(name)

    def input_standard(self, standard):
        self.find_element(*self.standard_ele).send_keys(standard)

    def input_producer(self, producer):
        self.find_element(*self.producer_ele).send_keys(producer)

    def input_supplier(self, unit=''):
        self.find_element(*self.supplier_ele).send_keys(unit)

    def select_part(self, unitProject, branch, usePart):
        Select(self.find_element(*self.select_unit_project_ele)).select_by_index(unitProject)
        Select(self.find_element(*self.select_branch_ele)).select_by_index(branch)
        self.find_element(*self.usePart_ele).send_keys(usePart)

    def input_admission(self, number, unit):
        self.find_element(*self.admissionQuantity_ele).send_keys(number)
        Select(self.find_element(*self.measurementUnits_ele)).select_by_value(unit)

    def input_guarantee(self, context=''):
        self.find_element(*self.guaranteeNo_ele).send_keys(context)

    def input_warranty(self, FileDir1=''):
        self.find_element(*self.input_warranty_ele).send_keys(FileDir1)

    # def input_certificate(self,):

    def selectPerson(self):
        self.find_element(*self.select_button).click()

        self.driver.switch_to_frame(self.find_element(*self.personList_frame_ele))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.select_person)).click()
        # search = (By.ID, 'searchContent')
        # self.find_element(*search).send_keys(u'刘')
        # self.find_element(*self.select_person).click()
        self.find_element(*self.person_confirm).click()
        self.driver.switch_to.parent_frame()  # 切回到上一个ifame
        # self.driver.switch_to_default_content()  # 切回主文档


    def click_confirm(self):
        self.find_element(*self.materials_confirm).click()

    def click_draft(self):
        self.find_element(*self.materials_draft).click()

    def new_mayerials(self):
        self.select_menu()
        self.select_toolbar()
        self.click_new()
        self.input_date(20171007)
        self.input_name('材料')
        self.input_standard('国歌')
        self.input_producer(producer='制作')
        self.input_supplier(unit='供应商')
        self.select_part(2, 1, '111')
        self.input_admission(12, '批')
        self.input_guarantee('哈哈哈')
        self.selectPerson()
        self.click_draft()
