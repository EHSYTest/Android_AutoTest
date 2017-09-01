from Page_Base import Page
import time

class OrderDetail(Page):

    order_id = ('by.xpath', "//android.view.View[contains(@content-desc, 'SO')]")
    back = ('by.id', 'com.ehsy.western:id/btn_title_left')

    def get_order_id(self):
        time.sleep(2)
        text = self.element_find(self.order_id).get_attribute('name')
        orderId = text[-20:]
        print(orderId)
        return orderId
