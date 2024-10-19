from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    template = loader.get_template("index1.html")
    return HttpResponse(template.render())


def home2PageView(request):
    template = loader.get_template("index2.html")
    return HttpResponse(template.render())

def home3PageView(request):
    template = loader.get_template("index3.html")
    return HttpResponse(template.render())
