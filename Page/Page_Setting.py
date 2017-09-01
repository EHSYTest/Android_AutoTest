from Page_Base import Page
from appium.webdriver.common.touch_action import TouchAction


class Setting(Page):
    logout_btn = ('by.name', '退出登录')
    change_environment_btn = ('by.id', 'com.ehsy.western:id/btn_title_right')
    environment_staging = ('by.name', 'staging环境')
    environment_production = ('by.name', '线上环境')

    phone_app = ('by.accessibility_id', 'Apps')
    ehsy_app = ('by.name', '西域')

    logout_confirm = ('by.name', '确　定')

    def change_environment(self, environment):
        el = self.element_find(self.change_environment_btn)
        TouchAction(self.driver).long_press(el).wait(1.5).perform()
        el.click()
        if environment == 'staging':
            self.element_find(self.environment_staging).click()
        elif environment == 'production':
            self.element_find(self.environment_production).click()

    def logout(self):
        self.element_find(self.logout_btn).click()
        self.element_find(self.logout_confirm).click()

"""
    def restart_app(self):
        self.element_find(self.phone_app).click()
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width*3/4, height/2, width/10, height/2)
        self.element_find(self.ehsy_app).click()
"""