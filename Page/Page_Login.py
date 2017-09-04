from Page_Base import Page
from selenium.common.exceptions import NoSuchElementException
from Page.Page_MyEhsy import MyEhsy
from Page_Setting import Setting


class Login(Page):

    login_from_myehsy = MyEhsy.login_btn
    clear_username = ('by.id', 'com.ehsy.western:id/clear_account_img_click')
    username = ('by.id', 'com.ehsy.western:id/input_account_et')
    password = ('by.id', 'com.ehsy.western:id/input_password_et')
    login_btn = ('by.name', '登录')

    def login(self, username, password):
        try:
            self.element_find(self.login_from_myehsy).click()
        except NoSuchElementException:
            MyEhsy(self.driver).click_setting()
            Setting(self.driver).logout()
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.driver.swipe(width/2, height/4, width/2, height/2)
            self.element_find(self.login_from_myehsy).click()
        finally:
            element = self.element_find(self.username).get_attribute('text')
            if element:
                self.element_find(self.clear_username).click()
            self.element_find(self.username).send_keys(username)
            self.element_find(self.password).send_keys(password)
            self.element_find(self.login_btn).click()
