from Page_Base import Page


class Home(Page):
    """首页"""
    search_input = ('by.id', 'com.ehsy.western:id/btn_search')
    search_btn = ('by.class_name', 'android.widget.ImageView')
    tools = ('by.id', 'com.ehsy.western:id/categoryIconImg')
    brand_ehs = ('by.class_name', 'android.widget.ImageView')
    my_ehsy = ('by.name', '我的西域')
    cart = ('by.name', '购物车')





