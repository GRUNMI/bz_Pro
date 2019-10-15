from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from dsy.dsy_case.common.base import Base

'''
新增设备报审
'''
class equipment(Base):
    menu_ele = (By.LINK_TEXT, "质量控制")
    equipment_ele = (By.LINK_TEXT, "设备")
    # frame标签
    right_iframe_ele = (By.ID, 'right_iframe')
    equipment_report_ele = (By.LINK_TEXT, "设备报审")
    new_equipment_ele = (By.CSS_SELECTOR, '.but-news-query.new-btn-yellow')
    name_ele = (By.ID, 'name')
    standard_ele = (By.ID, 'standard')
    purchaseContractNo_ele = (By.ID, 'purchaseContractNo')
    installContractNo_ele = (By.ID, 'installContractNo')
    producer_ele = (By.ID, 'producer')
    supplier_ele = (By.ID, 'supplier')
    code_ele = (By.ID, 'code')
    startDate_ele = (By.ID, 'startDate')
    packingNum_ele = (By.ID, 'packingNum')
    number_ele = (By.ID, 'number')
    measurementUnits_ele = (By.ID, 'measurementUnits')
    input_file_ele = (By.XPATH, "//*[@id='EQUIPMENT_ATTACHMENT']/div[2]/label")
    select_person_ele = (By.ID, 'ZB_COMFIRM_USER')

    personList_frame_ele = (By.CSS_SELECTOR, '.layui-layer-content>iframe ')
    # select_person = (By.XPATH, "//*[@id='nextorg']/li/div/dl/dd[1]/a")
    select_person = (By.LINK_TEXT, "刘馨儿（项目管理员）")
    person_confirm = (By.CSS_SELECTOR, '.new-btn-yellow')

    active_ele = (By.CSS_SELECTOR, '.submitBtn.new-btn-yellow')
    draft_ele = (By.CSS_SELECTOR, '.submitBtn.new-btn-gray')



    def select_menu(self):
        # 等待菜单按钮出来
        if WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.menu_ele)):
            '''选择菜单'''
            ActionChains(self.driver).move_to_element(self.find_element(*self.menu_ele)).perform()
            self.find_element(*self.equipment_ele).click()
        else:
            self.driver.quit()

        # 移动到用户名处，使菜单栏消失
        ActionChains(self.driver).move_to_element(
            self.find_element(By.CSS_SELECTOR, '.vam.ellipsis.maxW_100.fw-700')).perform()

    def select_equipment_report(self):
        self.frame_find_element(*self.right_iframe_ele)
        self.find_element(*self.equipment_report_ele).click()

    def click_new(self):
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.new_equipment_ele)).click()

    def input_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_ele)).send_keys(name)

    def input_standard(self, standard):
        self.find_element(*self.standard_ele).send_keys(standard)

    # 采购合同号
    def input_purchaseContractNo(self, purchaseContractNo=''):
        self.find_element(*self.purchaseContractNo_ele).send_keys(purchaseContractNo)

    # 安装合同号
    def input_installContractNo(self, installContractNo):
        self.find_element(*self.installContractNo_ele).send_keys(installContractNo)

    # 生产单位
    def input_producer(self, producer):
        self.find_element(*self.producer_ele).send_keys(producer)

    # 供应单位
    def input_supplier(self, supplier=''):
        self.find_element(*self.supplier_ele).send_keys(supplier)

    # 内部编号（梯号）
    def input_code(self, code=''):
        self.find_element(*self.code_ele).send_keys(code)

    # 出厂日期
    def input_startDate(self, startDate=None):
        self.remove_date_readonly(css_selector='#startDate')

        self.find_element(*self.startDate_ele).send_keys(startDate)

    # 装箱单号
    def input_packingNum(self, packingNum=''):
        self.find_element(*self.packingNum_ele).send_keys(packingNum)

    # 数量
    def input_number(self, number, measurementUnits):
        self.find_element(*self.number_ele).send_keys(number)
        self.find_element(*self.measurementUnits_ele).send_keys(measurementUnits)

    # 附件
    def input_file(self, filedir=''):
        self.find_element(*self.input_file_ele).send_keys(filedir)

    # 总包确认人
    def selectPerson(self):
        self.find_element(*self.select_person_ele).click()

        self.driver.switch_to_frame(self.find_element(*self.personList_frame_ele))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.select_person)).click()
        # search = (By.ID, 'searchContent')
        # self.find_element(*search).send_keys(u'刘')
        # self.find_element(*self.select_person).click()
        self.find_element(*self.person_confirm).click()
        self.driver.switch_to.parent_frame()  # 切回到上一个ifame
        # self.driver.switch_to_default_content()  # 切回主文档

    # 提交
    def click_confirm(self):
        self.find_element(*self.active_ele).click()

    # 草稿
    def click_draft(self):
        self.find_element(*self.draft_ele).click()

    def new_equipment(self):
        self.select_menu()
        self.select_equipment_report()
        self.click_new()
        self.input_name('你要的爱')
        self.input_standard('121212')
        self.input_purchaseContractNo()
        self.input_installContractNo(1212)
        self.input_producer('可不可以不勇敢')
        self.input_supplier()
        self.input_code()
        self.input_startDate(20171008)
        self.input_packingNum()
        self.input_number(2, '个')
        self.input_file()
        self.selectPerson()
