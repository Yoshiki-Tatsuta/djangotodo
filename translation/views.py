from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TranslationForm

# Create your views here.




def index(request):
    """翻訳画面"""
    # form = TranslationForm()
    # template = loader.get_template("translation/index.html")
    # context = {
    #     "form": form
    # }
    return render(request, "translation/index.html")