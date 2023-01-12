from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    """翻訳画面"""
    return render(request, "translation/index.html")


def translation(request):
    """翻訳結果表示"""
    if request.method == POST:
        values = request.POST.get('tr', None)
        ctx = {
            "value": values,
            }
    return render(request, "weather/getweather.html", ctx)