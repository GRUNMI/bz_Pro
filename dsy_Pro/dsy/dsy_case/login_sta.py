from .common.myunit import MyTest
from .page_object.loginPage import LoginPage
from .common.screenshot import screen_image
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import unittest
import time
class LoginTest(MyTest):
    '''dty登录测试'''
    def login_verify(self, username='', password=''):
        LoginPage(self.driver).login(username, password)

    def test_login1(self):
        '''用户名、密码正确登录'''
        self.login_verify(username='13733333333', password='88888888')
        po = LoginPage(self.driver)
        self.assertEqual(po.succeed_user(), "王明明")
        screen_image(self.driver, "登录界面")

        # self.project_ele = po.find_element(By.CSS_SELECTOR, '.companyDown.pointer')
        # self.project_ele = po.find_element(By.LINK_TEXT, '质量控制')
        # ActionChains(self.driver).move_to_element(self.project_ele).perform()
        # time.sleep(2)
        # # 获取当前账号所存在的工程名称
        # current_project = po.find_element(By.CSS_SELECTOR, '.show.fw-700.ellipsis')
        # print(current_project.text)
        # projects_ele = po.find_elements(By.CSS_SELECTOR, "div[class='ellipsis']")
        # for project_text in projects_ele:
        #     print(project_text.text)
        #     if project_text.text == "哈工大监理工程":
        #         project_text.click()
        #         break
        #     else:
        #         print("NO Find")
        #         continue


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(LoginTest('test_login1'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
    # unittest.main()
