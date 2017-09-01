from Page_Base import Page
from selenium.common.exceptions import ElementNotVisibleException
import time


class ProductList(Page):
    """产品列表、大图、品牌页、sku搜索结果页"""
    list_cart_btn = ('by.id', 'com.ehsy.western:id/cart_iv')
    back = ('by.id', 'com.ehsy.western:id/back_iv')
    product_img = ('by.id', 'com.ehsy.western:id/commodity_iv')



