from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.edit import FormView
from .apiData import data
from .apiData import kingdee
from .apiData import supplierApis
from .forms import kingdeeForm
from .forms import searchGoodForm
from .forms import modinvForm
from .forms import searchOrderForm
from .forms import ihaixieForm
from .forms import creatOrderForm


def index(request):  # api测试主页面
    context = {'apis': data.allApi}
    return render(request, 'apiTests/index.html', context)


class kingdeeView(FormView):
    template_name = "apiTests/kingdee.html"
    form_class = kingdeeForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        api = kingdee.apis(post_data)
        response = api.res()
        return JsonResponse(response)

    def get_context_data(self, **kwargs):
        self.request.current_app = self.request.resolver_match.namespace
        context = super(kingdeeView, self).get_context_data(**kwargs)
        if self.kwargs['num'] == '1':
            postUrl = 1
            data.kingdeePayload['method'] = 'kingdee.items.get'
            context['otherform'] = searchGoodForm()
        elif self.kwargs['num'] == '2':
            postUrl = 2
            data.kingdeePayload['method'] = 'kingdee.item.quantity.update'
            context['otherform'] = modinvForm()
        elif self.kwargs['num'] == '3':
            postUrl = 3
            data.kingdeePayload['method'] = 'kingdee.trades.get'
            context['otherform'] = searchOrderForm()
        else:
            data.kingdeePayload['method'] = '获取数据错误'
        context['postUrl'] = postUrl
        context['apis'] = data.allApi
        context['sysform'] = kingdeeForm(data.kingdeePayload)
        return context


class ihaixieView(FormView):
    template_name = 'apiTests/ihaixie.html'
    form_class = ihaixieForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        api = supplierApis.apis(post_data)
        response = api.creatOrder()
        return JsonResponse(response)

    def get_context_data(self, **kwargs):
        self.request.current_app = self.request.resolver_match.namespace
        context = super(ihaixieView, self).get_context_data(**kwargs)
        if self.kwargs['num'] == '1':
            postUrl = 1
            data.ihaixieUser['url'] = 'http://www.zydong.cc/shop/index.php?act=member_order&op=addOrder'  # 请求地址url
            context['otherform'] = creatOrderForm()
        # elif self.kwargs['num'] == '2':
        #     postUrl = 2
        #     data.kingdeePayload['method'] = 'kingdee.item.quantity.update'
        #     context['otherform'] = modinvForm()
        # elif self.kwargs['num'] == '3':
        #     postUrl = 3
        #     data.kingdeePayload['method'] = 'kingdee.trades.get'
        #     context['otherform'] = searchOrderForm()
        # else:
        #     data.kingdeePayload['method'] = '获取数据错误'
        context['postUrl'] = postUrl  # 表单提交地址
        context['apis'] = data.allApi
        context['sysform'] = ihaixieForm(data.ihaixieUser)
        return context
