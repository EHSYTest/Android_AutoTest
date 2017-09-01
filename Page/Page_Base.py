import requests
from configobj import ConfigObj


class Page():

    def __init__(self, driver):
        self.driver = driver

    def element_find(self, element):
        if element[0] == 'by.id':
            element_find = self.driver.find_element_by_id(element[1])
        if element[0] == 'by.xpath':
            element_find = self.driver.find_element_by_xpath(element[1])
        if element[0] == 'by.class_name':
            element_find = self.driver.find_element_by_class_name(element[1])
        if element[0] == 'by.name':
            element_find = self.driver.find_element_by_name(element[1])
        if element[0] == 'by.tag_name':
            element_find = self.driver.find_element_by_tag_name(element[1])
        if element[0] == 'by.link_text':
            element_find = self.driver.find_element_by_link_text(element[1])
        if element[0] == 'by.partial_link_text':
            element_find = self.driver.find_element_by_partial_link_text(element[1])
        if element[0] == 'by.accessibility_id':
            element_find = self.driver.find_element_by_accessibility_id(element[1])
        return element_find

    def elements_find(self, element):
        if element[0] == 'by.id':
            elements_find = self.driver.find_elements_by_id(element[1])
        if element[0] == 'by.xpath':
            elements_find = self.driver.find_elements_by_xpath(element[1])
        if element[0] == 'by.class_name':
            elements_find = self.driver.find_elements_by_class_name(element[1])
        if element[0] == 'by.name':
            elements_find = self.driver.find_elements_by_name(element[1])
        if element[0] == 'by.tag_name':
            elements_find = self.driver.find_elements_by_tag_name(element[1])
        if element[0] == 'by.link_text':
            elements_find = self.driver.find_elements_by_link_text(element[1])
        if element[0] == 'by.partial_link_text':
            elements_find = self.driver
        if element[0] == 'by.accessibility_id':
            elements_find = self.driver.find_elements_by_accessibility_id(element[1])
        return elements_find

    @staticmethod
    def cancel_order(orderId, environment='staging', userId='508107841'):
        if environment == 'staging':
            url = 'http://oc-staging.ehsy.com/orderCenter/cancel'
        elif environment == 'production':
            url = 'http://oc.ehsy.com/orderCenter/cancel'
        data = {'orderId': orderId, 'userId': userId}
        r = requests.post(url, data=data)
        result = r.json()
        print(result['message'])
        assert result['message'] == '订单取消申请提交成功'

    @staticmethod
    def config_reader(file, section, option):
        config = ConfigObj('../config/' + file)
        content = config[section][option]
        return content
