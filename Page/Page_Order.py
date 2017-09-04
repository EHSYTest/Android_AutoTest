from Page_Base import Page


class Order(Page):

    choose_invoice = ('by.id', 'com.ehsy.western:id/invoice_info_tv')
    submit_order = ('by.id', 'com.ehsy.western:id/create_order_btn')

    # 选择发票页面
    none_invoice = ('by.name', '　不开发票')
    normal_invoice = ('by.name', '　17%普通发票')
    vat_invoice = ('by.name', '　17%增值税发票')
    invoice_choose = ('by.name', '请选择发票信息')
    address_choose = ('by.name', '寄送地址')
    first_normal_invoice = ('by.id', 'com.ehsy.western:id/rootCompany')
    first_vat_invoice = ('by.id', 'com.ehsy.western:id/tv_invoice_name')
    first_address = ('by.id', 'com.ehsy.western:id/address_name_txt')
    normal_invoice_confirm = ('by.name', '确定')
    invoice_confirm = ('by.name', '确定')

    def choose_vat_invoice(self):
        self.element_find(self.choose_invoice).click()
        self.element_find(self.vat_invoice).click()
        self.element_find(self.invoice_choose).click()
        self.element_find(self.first_vat_invoice).click()
        self.element_find(self.address_choose).click()
        self.element_find(self.first_address).click()
        self.element_find(self.invoice_confirm).click()

    def choose_normal_invoice(self):
        self.element_find(self.choose_invoice).click()
        self.element_find(self.normal_invoice).click()
        self.element_find(self.invoice_choose).click()
        self.element_find(self.first_normal_invoice).click()
        self.element_find(self.normal_invoice_confirm).click()
        self.element_find(self.address_choose).click()
        self.element_find(self.first_address).click()
        self.element_find(self.invoice_confirm).click()

    def choose_none_invoice(self):
        self.element_find(self.choose_invoice).click()
        self.element_find(self.none_invoice).click()
        self.element_find(self.invoice_confirm).click()

