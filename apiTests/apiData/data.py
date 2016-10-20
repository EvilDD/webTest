import collections

allApi = collections.OrderedDict()
allApi['现货采购'] = [
    ['创建订单', '/api/ihaixie/1'],
    ['查看订单状态', '/api/ihaixie/2'],
    ['获取商品库存', '/api/ihaixie/3']
]
allApi['供应商应用'] = [
    ['商品新增', '/api/supplier/1'],
    ['消费税列表', '/api/supplier/2'],
    ['商品类型', '/api/supplier/3'],
    ['品牌数据', '/api/supplier/4'],
    ['商品单位', '/api/supplier/5'],
    ['发货地/商品来源', '/api/supplier/6'],
    ['商品规格/属性', '/api/supplier/7']
]
allApi['金蝶进销存'] = [
    ['下载商品', '/api/kingdee/1'],
    ['修改商品库存', '/api/kingdee/2'],
    ['查询交易数据', '/api/kingdee/3']
]

kingdeePayload = {
    'post_url': "http://www.ihaixie.com/shop/index.php?act=kingdeeApi&op=api",
    'method': "",
    'app_key': 'www.ihaixie.com',
    'session': 'CxhJKaYV6C3mP5TYQAGII63ZSQgqvtrg',
    'v': '1.0',
    'timestamp': '',
    'format': 'json',
    'partner_id': 'KingdeeOrder100',
    'shopid': 'ihaixie',
}  # 必要系统参数
