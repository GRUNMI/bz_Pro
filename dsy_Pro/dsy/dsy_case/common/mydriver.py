from selenium import webdriver
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def browser():
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS(executable_path=r"F:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    # driver = webdriver.Remote("http://localhost:4446/wd/hub", desired_capabilities=DesiredCapabilities.HTMLUNIT)

    return driver
if __name__ == '__main__':
    dr = browser()
    dr.set_window_size(1300, 1000)
    # driver.maximize_window()
    print('succeed')
    time.sleep(1)
    dr.quit()
