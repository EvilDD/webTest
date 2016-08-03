from django.http import HttpResponseNotFound


def index(request):
    html = "这是主页面,请加api后缀!"
    return HttpResponseNotFound(html)
