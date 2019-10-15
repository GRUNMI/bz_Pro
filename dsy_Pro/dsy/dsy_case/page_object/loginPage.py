import time
from selenium.webdriver.common.by import By
from dsy.dsy_case.common.base import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage(Base):

    url_login_button_ele = (By.LINK_TEXT, "登录")
    username_ele = (By.CSS_SELECTOR, "div>ul>li>input")
    # login_username = (By.CSS_SELECTOR, "input")
    password_ele = (
        By.CSS_SELECTOR,
        "input[type='password'][placeholder='密码（8~12位字符，区分大小写）']")
    click_login_button = (By.CSS_SELECTOR, "input[type='button'][value='登录']")

    def click_browser_login_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.url_login_button_ele)).click()
        # self.find_element(*self.url_login_button_ele).click()

    def input_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_ele)).send_keys(username)
        # self.find_element(*self.username_ele).send_keys(username)

    def input_pwd(self, pwd):
        self.find_element(*self.password_ele).send_keys(pwd)

    def click_login_btn(self):
        self.find_element(*self.click_login_button).click()

    def login(self, username='username', pwd='password'):
        '''

        :param username:
        :param pwd:
        :return:
        '''
        self.open_broser()
        self.click_browser_login_btn()
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login_btn()

    succeed_username = (By.CSS_SELECTOR, '.vam.ellipsis.maxW_100.fw-700')

    def succeed_user(self):
        return self.find_element(*self.succeed_username).text
