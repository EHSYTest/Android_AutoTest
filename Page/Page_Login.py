from Page_Base import Page


class Login(Page):

    clear_username = ('by.id', 'com.ehsy.western:id/clear_account_img_click')
    username = ('by.id', 'com.ehsy.western:id/input_account_et')
    password = ('by.id', 'com.ehsy.western:id/input_password_et')
    login_btn = ('by.name', '登录')

    def login(self, username, password):
        element = self.element_find(self.username).get_attribute('text')
        if element:
            self.element_find(self.clear_username).click()
        self.element_find(self.username).send_keys(username)
        self.element_find(self.password).send_keys(password)
        self.element_find(self.login_btn).click()
