from Page_Base import Page
import time
from selenium.common.exceptions import NoSuchElementException


class OrderDetail(Page):

    # order_id = ('by.xpath', "//android.view.View[contains(@content-desc, 'SO')]")
    order_id = ('by.android_uiautomator', 'new UiSelector().descriptionContains("SO")')
    back = ('by.id', 'com.ehsy.western:id/btn_title_left')

    def get_order_id(self):
        while True:
            try:
                el = self.element_find(self.order_id)
                break
            except NoSuchElementException:
                time.sleep(0.2)
                continue
        text = el.get_attribute('name')
        orderId = text[-20:]
        print(orderId)
        return orderId
