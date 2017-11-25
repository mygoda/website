from django.shortcuts import render, render_to_response
from django.template import RequestContext

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
    return render_to_response("index.html", {"types": type_shops}, RequestContext(req))


def detail(req, shop_id):
    """
        详情
    :param req:
    :param shop_id:
    :return:
    """
    return render_to_response("detail.html")
