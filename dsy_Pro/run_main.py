import unittest
import sys
import time
from dsy.report.HTMLTestRunner import HTMLTestRunner
from dsy.dsy_case.page_object.contractorF.contractF.localeChange_sta import localeChangeTest
from dsy.dsy_case.page_object.contractorZ.contractZ.localeChangeF_sta import localeChangeFTest

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(localeChangeTest('test_localeChange1'))
    suit.addTest(localeChangeFTest('test_localeChangeF1'))

    file_dir = sys.path[0]  # 当前路径
    nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = nowTime + 'result.html'
    file_path = file_dir + '\\dsy\\report\\' + filename
    print(file_path)
    # fp = open(file_path, 'wb')
    # runner = HTMLTestRunner(stream=fp, verbosity=2, title='智慧工程自动化测试报告', description='环境：python3 selenium2 win10 浏览器：Chrome')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
