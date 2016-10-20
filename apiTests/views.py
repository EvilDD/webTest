from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import FormView
from .apiData import data
from .forms import kingdeeForm
from .forms import searchGoodForm
from .forms import modinvForm
from .forms import searchOrderForm
from .apiData import kingdee


def index(request):  # api测试主页面
    context = {'apis': data.allApi}
    return render(request, 'apiTests/index.html', context)


class kingdeeView(FormView):
    template_name = "apiTests/kingdee.html"
    form_class = kingdeeForm

    success_url = '/'

    # def form_valid(self, form):
    #     # form.send_email()
    #     return super(kingdeeView, self).form_valid(form)

    # # def get(self, request, *args, **kwargs):
    # #     isExistUrl = True  # 存在该api的url
    # #     if isExistUrl:
    # #         if api_name == 'searchGoods':
    # #             self.payloadB['method'] = 'abcccccc'
    # #         elif api_name = ''
    # #         return super(kingdeeView, self).get(request, api_name, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        self.post_data = request.POST
        api = kingdee.apis(self.post_data)
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
