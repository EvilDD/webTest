import requests
import hashlib
import time


class apis:
    def __init__(self, data):
        self.postUrl = data['post_url']
        self.payload = data.copy()  # django的queryDict只能用copy才能修改字典
        del self.payload['csrfmiddlewaretoken']
        del self.payload['post_url']
        self.payload['timestamp'] = repr(
            int(time.mktime(time.strptime(self.payload['timestamp'], '%Y-%m-%d %H:%M:%S'))))
        self.addSign()

    def res(self):
        r = requests.post(self.postUrl, data=self.payload)
        return r.json()

    def addSign(self):  # 加签名返回payload
        # payload = dict(payloadM, **dic)  # 合并字典
        tmp = sorted(self.payload.items(), reverse=False)
        # print(tmp)
        sign = ''
        for t in tmp:
            s = t[0] + t[1]
            sign += s
        signString = '8eI7UftYwMXW1FRf'
        sign = signString + sign + signString
        m = hashlib.md5(sign.encode(encoding='utf-8'))
        sign = m.hexdigest().upper()
        self.payload['sign'] = sign
        # print(self.payload)
