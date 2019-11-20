from selenium import webdriver
from weather.common.test_suite import TestSuite

class PageObject(TestSuite):
    xpaths = { 'search' : '//*[@name="search"]',
               'list_of_definitions' : "//ol",
               'submitButton' : "//input[@name='login']"
             }

    @classmethod
    def setUpClass(cls):
        conf = cls.readConfig()
        cls.base_page = conf['frontend']['host']
        cls.wd = webdriver.Chrome()
        cls.wd.get(cls.base_page)

    def setUp(self):
        self.wd.get(self.base_page)

    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()


    def input_data(self, xpath, data):
        element = self.wd.find_element_by_xpath(xpath)
        element.click()
        element.send_keys(data)
        element.send_keys(u'\ue007')


