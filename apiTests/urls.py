from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ihaixie/(?P<num>\d+)$', views.ihaixieView.as_view(), name='ihaixie_api'),
    url(r'^kingdee/(?P<num>\d+)$', views.kingdeeView.as_view(), name='kingdee_api'),
    # url(r'^supplier/(?P<api_name>\w+)$', views.supplierView.as_view(), name='supplier_api'),
    # url(r'test', views.test.as_view())
]
