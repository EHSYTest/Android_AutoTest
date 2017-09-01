from Page_Base import Page


class Cart(Page):

    go_to_order = ('by.id', 'com.ehsy.western:id/createOrderBtn')
    add_btn = ('by.name', '+')
    sub_btn = ('by.name', '-')
    quantity_input = ('by.id', 'com.ehsy.western:id/amountTxt')
