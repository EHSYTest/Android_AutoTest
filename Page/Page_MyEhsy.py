from Page_Base import Page


class MyEhsy(Page):

    login_btn = ('by.id', 'com.ehsy.western:id/login_tv_click')
    setting = ('by.name', '设置')
    home_page = ('by.name', '首页')

    def click_setting(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width/2, height/2, width/2, height/4)
        self.element_find(self.setting).click()
