import requests
import json

url = 'http://www.zydong.cc/supplierApi/index.php?'
pubData = {
    'CUSTOMERCODE': 'gys001',
    'REQUESTTIME': '7b6a0ed1e7b6a0e1e7d823529b3a6860a6eeedd1e',
    'data': ''
}


def digestData(**dic):
    print(dic, type(dic))


def decodeStr(s):
    pass


def saleTaxList():
    saleurl = url + 'act=goods&op=getSaleTax'
    r = requests.post(saleurl, pubData)
    print(r.json())


def test():
    url = 'http://www.zydong.cc/supplierApi/index.php?act=test&op=goodInsert'
    # url = 'http://www.zydong.cc/supplierApi/index.php?act=test&op=getGoodsClass'
    r = requests.get(url)
    print(r.json())

if __name__ == '__main__':
    test()
