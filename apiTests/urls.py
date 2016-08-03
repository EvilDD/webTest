from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^developer/(?P<api_name>\w+)$', views.developerView.as_view(), name='developer_api'),
    url(r'^kingdee/(?P<api_name>\w+)$', views.kingdeeView.as_view(), name='kingdee_api'),
    # url(r'^supplier/(?P<api_name>\w+)$', views.supplierView.as_view(), name='supplier_api'),
]
