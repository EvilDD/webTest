import requests
import json


class apis:
    def __init__(self, data):
        self.payload = data.copy()
        del self.payload['csrfmiddlewaretoken']

    def creatOrder(self):
        url = self.payload['url']
        del self.payload['url']
        payload = {
            'u': self.payload['u'],
            'p': self.payload['p'],
            'o[0][reference_number]': self.payload['reference_number'],
            'o[0][reciver_name]': self.payload['reciver_name'],
            'o[0][reciver_id_number]': self.payload['reciver_id_number'],
            'o[0][reciver_mobile]': self.payload['reciver_mobile'],
            'o[0][reciver_tel]': self.payload['reciver_tel'],
            'o[0][shipping_fee]': self.payload['shipping_fee'],
            'o[0][shipping_type]': self.payload['shipping_type'],
            'o[0][postcode]': self.payload['postcode'],
            'o[0][province]': self.payload['province'],
            'o[0][city]': self.payload['city'],
            'o[0][county]': self.payload['county'],
            'o[0][address]': self.payload['address'],
            'o[0][sender_name]': self.payload['sender_name'],
            'o[0][sender_tel]': self.payload['sender_tel'],
            'o[0][goods_serial]': self.payload['goods_serial'],
            'o[0][goods_num]': self.payload['goods_num'],
            'o[0][customs_goods_price]': self.payload['customs_goods_price']
        }
        r = requests.post(url, data=payload)
        return r.json()
