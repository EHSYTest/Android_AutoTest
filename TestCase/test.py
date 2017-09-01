import sys
sys.path.append('../Page')
import unittest
from HTMLTestRunner import HTMLTestRunner
from appium import webdriver
from Page_Base import Page
from Page_Cart import Cart
from Page_Home import Home
from Page_Order import Order
from Page_CategoryTools import CategoryTools
from Page_ProductList import ProductList
from Page_ProductContent import ProductContent
from Page_MyEhsy import MyEhsy
from Page_Login import Login
from Page_Pay import Pay
from Page_OrderDetail import OrderDetail
from Page_Setting import Setting


class TestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.ehsy.western'
        desired_caps['appActivity'] = 'com.ehsy.western.MainTabActivity'
        desired_caps['newCommandTimeout'] = 600
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        self.page = Page(self.driver)
        self.cart = Cart(self.driver)
        self.home = Home(self.driver)
        self.order = Order(self.driver)
        self.category_tools = CategoryTools(self.driver)
        self.product_list = ProductList(self.driver)
        self.product_content = ProductContent(self.driver)
        self.my_ehsy = MyEhsy(self.driver)
        self.login = Login(self.driver)
        self.pay = Pay(self.driver)
        self.order_detail = OrderDetail(self.driver)
        self.setting = Setting(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        """
        self.home.element_find(self.home.my_ehsy).click()
        self.my_ehsy.click_setting()
        self.setting.change_environment(environment=self.environment)
        self.setting.element_find(self.setting.ehsy_app).click()
        """

    def test_order_1(self):
        """列表页入口-个人用户下单-不开票"""
        login_name = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.element_find(self.home.my_ehsy).click()
        self.my_ehsy.element_find(self.my_ehsy.login_btn).click()
        self.login.login('Rick自动化测试', '111qqq')
        self.my_ehsy.element_find(self.my_ehsy.home_page).click()
        self.home.element_find(self.home.tools).click()
        self.category_tools.element_find(self.category_tools.category_tools_suit).click()
        self.product_list.element_find(self.product_list.list_cart_btn).click()
        self.product_list.element_find(self.product_list.back).click()
        self.category_tools.element_find(self.category_tools.back).click()
        self.home.element_find(self.home.cart).click()
        self.cart.element_find(self.cart.go_to_order).click()
        self.order.choose_none_invoice()
        self.order.element_find(self.order.submit_order).click()
        self.pay.element_find(self.pay.pay_way_bank).click()
        self.pay.element_find(self.pay.query_order).click()
        orderId = self.order_detail.get_order_id()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单
        self.order_detail.element_find(self.order_detail.back).click()
        self.home.element_find(self.home.my_ehsy).click()
        self.my_ehsy.click_setting()
        self.setting.logout()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  TestCase('test_order_1'),
                  ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/order_android.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='Android自动化——测试报告', description='测试情况')
    runner.run(suit)
    file.close()
