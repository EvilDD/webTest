from django import forms


class kingdeeForm(forms.Form):
    style = forms.TextInput(attrs={
        # 'disabled': 'disabled',
        'size': 30,
        'readonly': 'readonly',
    })
    # 以下是系统特定值参数
    post_url = forms.URLField(label='请求url', widget=style)
    method = forms.CharField(label='调用api', widget=style, required=False)
    app_key = forms.CharField(label='应用密钥', widget=style)
    session = forms.CharField(label='会话', widget=style)
    v = forms.CharField(label='版本', widget=style)
    format = forms.CharField(label='格式', widget=style)
    partner_id = forms.CharField(label='合作企业id', widget=style)
    shopid = forms.CharField(label='商城id', widget=style)
    timestamp = forms.DateTimeField(label='时间戳', widget=style, required=False)


class searchGoodForm(forms.Form):
    SALE_OR_STOCK_CHOICES = (
        ('onsale', '上架'),
        ('instock', '下架')
    )
    start_time = forms.DateTimeField(label='开始时间', required=False)
    end_time = forms.DateTimeField(label='结束时间', required=False)
    page_no = forms.IntegerField(label='页数', required=False, min_value=0)
    page_size = forms.IntegerField(label='每页条数', required=False, min_value=0)
    status = forms.ChoiceField(label='上下架', choices=SALE_OR_STOCK_CHOICES)
    num_iid = forms.CharField(label='商品数字Id', required=False)


class modinvForm(forms.Form):
    TYPE_CHOICE = (
        (1, '全量更新'),
        (2, '增量更新')
    )
    num_iid = forms.CharField(label='商品数字Id')
    quantity = forms.IntegerField(label='库存修改值', min_value=0)
    sku_id = forms.CharField(label='sku的数字id', required=False)
    type = forms.ChoiceField(label='库存更新方式', choices=TYPE_CHOICE)


class searchOrderForm(forms.Form):
    PAY_STATUS_CHOICE = (
        ('TRADE_WAIT_BUYER_PAY', '没有付款'),
        ('TRADE_SELLER_SEND_GOODS', '已付款'),
        ('TRADE_WAIT_BUYER_CONFIRM_GOODS', '已发货'),
        ('TRADE_FINISHED', '交易完成'),
        ('TRADE_AUTOMATIC_CLOSED', '交易关闭')
    )
    TIME_TYPE_CHOICE = (
        (1, '创建时间'),
        (2, '修改时间')
    )
    start_time = forms.DateTimeField(label='开始时间', required=False)
    end_time = forms.DateTimeField(label='结束时间', required=False)
    page_no = forms.IntegerField(label='页码', required=False, min_value=0)
    page_size = forms.IntegerField(label='每页条数', required=False, min_value=0)
    use_has_next = forms.BooleanField(label='是否启用分页', required=False)
    status = forms.ChoiceField(label='交易状态', choices=PAY_STATUS_CHOICE)
    datatype = forms.ChoiceField(label='时间类型', choices=TIME_TYPE_CHOICE)
    tid = forms.CharField(label='订单号', required=False)


class ihaixieForm(forms.Form):
    style = forms.TextInput(attrs={
        # 'disabled': 'disabled',
        # 'size': 30,
        'readonly': 'readonly',
    })
    url = forms.CharField(label='请求的url', widget=style)
    u = forms.CharField(label='用户名', widget=style)
    p = forms.CharField(label='密码', widget=style)


class creatOrderForm(forms.Form):
    SHIPPING_TYPE_CHOICE = (
        (1, 'test'),

    )
    reference_number = forms.CharField(label='订单号')
    reciver_name = forms.CharField(label='收件人姓名')
    reciver_id_number = forms.CharField(label='身份证号码')
    reciver_mobile = forms.CharField(label='收件人手机号码', required=False)
    reciver_tel = forms.CharField(label='收件人电话号码', required=False)
    shipping_fee = forms.FloatField(label='物流费用', required=False, min_value=0)
    shipping_type = forms.ChoiceField(label='清关物流方式', choices=SHIPPING_TYPE_CHOICE)
    postcode = forms.CharField(label='收件人邮编')
    province = forms.CharField(label='收件人省份')
    city = forms.CharField(label='收件人城市')
    county = forms.CharField(label='收件人区县')
    address = forms.CharField(label='收件人地址')
    sender_name = forms.CharField(label='寄件人姓名')
    sender_tel = forms.CharField(label='寄件人电话')
    goods_serial = forms.CharField(label='商品国际编码')
    goods_num = forms.IntegerField(label='商品购买数量', min_value=0)
    customs_goods_price = forms.FloatField(label='商品价格', required=False, min_value=0)
