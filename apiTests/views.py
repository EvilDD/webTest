from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .apiData import kingdee
# Create your views here.
# from django.http import HttpResponse
# from django.template import RequestContext, loader


def index(request):  # api测试主页面
    return render(request, 'apiTests/index.html', {'isDisplay': 'False'})


# class developerView(TemplateView):
#     template_name = "apiTests/kingdee.html"

#     def get_context_data(self, **kwargs):
#         self.request.current_app = self.request.resolver_match.namespace
#         context = super(kingdeeView, self).get_context_data(**kwargs)
#         context['respond'] = "空"
#         return context


class kingdeeView(TemplateView):
    template_name = "apiTests/kingdee.html"
    payloadB = {}

    def get(self, request, api_name, *args, **kwargs):
        if api_name == 'searchGoods':
            self.payloadB['method'] = 'abc'
        return TemplateView(request, *args, **kwargs)
        # return render(request, self.template_name)

    def get_context_data(self, api_name, **kwargs):
        self.request.current_app = self.request.resolver_match.namespace
        context = super(kingdeeView, self).get_context_data(**kwargs)
        context['apiName'] = api_name
        context['apiUrl'] = kingdee.url
        context['systemData'] = kingdee.payloadM
        context['apiData'] = self.payloadB
        return context


# class supplierView(TemplateView):
#     template_name = "apiTests/kingdee.html"

#     def get_context_data(self, **kwargs):
#         self.request.current_app = self.request.resolver_match.namespace
#         context = super(kingdeeView, self).get_context_data(**kwargs)
#         context['respond'] = "空"
#         return context
