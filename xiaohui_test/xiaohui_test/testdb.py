#coding:utf-8

from django.http import HttpResponse
from TZmyApp.models import Test


def testdb(request):
    test1=Test(name='xiaohui')
    test1.save()
    return HttpResponse('<p>数据添加成功！</p>')