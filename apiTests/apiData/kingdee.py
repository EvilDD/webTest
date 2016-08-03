import requests
import hashlib


url = "http://www.ihaixie.com/shop/index.php?act=kingdeeApi&op=api"

payloadM = {
    'app_key': 'www.ihaixie.com',
    'session': 'CxhJKaYV6C3mP5TYQAGII63ZSQgqvtrg',
    'v': '1.0',
    'timestamp': '',
    'format': 'json',
    'partner_id': 'KingdeeOrder100',
    'shopid': 'ihaixie',
}  # 必要系统参数


def res(payload):
    r = requests.post(url, data=payload)
    return r.json()


def addSign(dic):  # 加签名返回payload
    payload = dict(payloadM, **dic)  # 合并字典
    tmp = sorted(payload.items(), reverse=False)
    sign = ''
    for t in tmp:
        s = t[0] + t[1]
        sign += s
    signString = '8eI7UftYwMXW1FRf'
    sign = signString + sign + signString
    m = hashlib.md5(sign.encode(encoding='utf-8'))
    sign = m.hexdigest().upper()
    payload['sign'] = sign
    return payload


def searchGood(data):  # 查询商品api
    payloadB = {
        'method': data['method'],
        'start_time': data['start_time'],
        'end_time': data['end_time'],
        'page_no': data['page_no'],
        'page_size': data['page_size'],
        'status': data['status'],
        "num_iid": data['num_iid'],
    }
    payload = addSign(payloadB)
    return payload


def modinv():  # 修改库存api
    payloadB = {
        'method': 'kingdee.item.quantity.update',
        'num_iid': '30S4MLMS7TPWR',
        'quantity': '1',
        'sku_id': '1786',
        'type': '1',
    }
    payload = addSign(payloadB)
    print(payload)
    r = requests.post(url, data=payload)
    return r.json()


def searchOrder():  # 查找交易数据api
    payloadB = {
        'method': 'kingdee.trades.get',
        'start_time': '2016-05-29 00:00:00',
        'end_time': '2016-05-30 18:00:00',
        'page_no': '3',
        'page_size': '1',
        'use_has_next': 'true',
        'status': 'TRADE_AUTOMATIC_CLOSED',
        'datetype': '1',
        'tid': 'HXW8000000002470902',
    }
    payload = addSign(payloadB)
    r = requests.post(url, data=payload)
    return r.json()

if __name__ == '__main__':
    goods = modinv()
    print(goods)
