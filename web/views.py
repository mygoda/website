from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


from web.models import Banner, Shop, Type

# Create your views here.


def index(req):
    """
        首页
    :param req:
    :return:
    """
    types = Type.objects.all()
    type_shops = [type.to_json() for type in types]
    banners = Banner.objects.all()
    result = {
        "banners": [banner.to_json() for banner in banners],
        "types": type_shops
    }
    return render_to_response("index.html", result, RequestContext(req))


def query(req):
    """
        商店列表
    :param req:
    :return:
    """
    type_id = req.GET.get("type_id")
    shops = Shop.objects.filter(type_id=type_id)
    types = Type.objects.all()
    result = {
        "shops": shops,
        "type_id": type_id,
        "types": types
    }
    return render_to_response("shops.html", result, RequestContext(req))


def detail(req, shop_id):
    """
        详情
    :param req:
    :param shop_id:
    :return:
    """
    return render_to_response("detail.html")
