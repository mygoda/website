# coding=utf-8
from django.db import models

# Create your models here.


class Banner(models.Model):

    name = models.CharField(u"名称", max_length=16)
    img = models.CharField(u"图片链接", max_length=255)
    url = models.CharField(u"跳转链接", max_length=255)
    pri = models.IntegerField(u"优先级", default=0, help_text=u"数字越小，优先级越高")

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "img": self.img,
            "url": self.url
        }

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
        ordering = ('pri',)


class Type(models.Model):
    """
        类型
    """
    name = models.CharField(u"名称", max_length=32)

    def __str__(self):
        return self.name

    def shops(self):
        return self.shop_set.all()

    def list_json(self):
        return {
            "name": self.name,
            "id": self.id
        }

    def to_json(self):
        index_shops = self.shops()[:3]
        return {
            "id": self.id,
            "name": self.name,
            "shops": [shop.list_json() for shop in index_shops]
        }

    class Meta:
        verbose_name = '店铺类型'
        verbose_name_plural = '店铺类型'


class Shop(models.Model):
    """
        店面
    """

    name = models.CharField(u"店面名称", max_length=32)
    tag = models.CharField(u"标签", max_length=128, null=True, blank=True)
    type = models.ForeignKey(Type, verbose_name=u"类型")
    pri = models.IntegerField(u"优先级", default=0, help_text=u"数字越小，优先级越高")
    img = models.CharField(u"图片", max_length=255, null=True, blank=True)
    desc = models.TextField(u"详细描述", null=True, blank=True, help_text=u"目前是公众账号跳转连接")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '店面'
        verbose_name_plural = '店面'
        ordering = ('pri',)

    def list_json(self):
        """
            列表返回
        :return:
        """
        return {
            "id": self.id,
            "name": self.name
        }

    def to_json(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "type": self.type.id,
            "img": self.img,
        }
