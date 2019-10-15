class Base(object):
    base_url = "http://dsy.10333.com/"

    def __init__(self, driver, url=base_url):
        self.url = url
        self.driver = driver

    def open_broser(self):
        # url = self.url
        self.driver.get(self.url)
        assert self.driver.current_url == self.url, 'Did not land on %s' % self.url

    def find_element(self, *local):
        return self.driver.find_element(*local)

    def find_elements(self, *local):
        return self.driver.find_elements(*local)

    def switch_frame(self, *local):
        return self.driver.switch_to.frame(self.find_element(*local))

    # 滚动到底部
    def scroll_bottom(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        return self.driver.execute_script(js)

    # 滚动到顶部
    def scroll_tol(self):
        js = "window.scrollTo(0,0)"
        return self.driver.execute_script(js)

    # 滚动到元素处
    def scroll_go_to_ele(self, *loc):
        target = self.find_element(*loc)
        return self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 移除日期属性readonly
    def remove_date_readonly(self, css_selector):
        # js = "$('input[id=%s]').removeAttr('readonly')" % id
        # js = "document.getElementById('%s').removeAttribute('readonly')" % id
        js = "document.querySelector('%s').removeAttribute('readonly')" % css_selector
        self.driver.execute_script(js)

    # 移除日期属性data-reactid
    def remove_date_data_reactid(self, css_selector):
        js = "document.querySelector('%s').removeAttribute('data-reactid')" % css_selector
        self.driver.execute_script(js)

