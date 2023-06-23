from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from deep_translator import GoogleTranslator

# Create your views here.

def index(request): 
    if request.method == 'POST':
        if 'gel-ja' == request.POST['select-gel']:
            input_data = request.POST['trans']
            trans_data = GoogleTranslator(source='auto', target='ja').translate(input_data)      
            return render(request, 'translation/index.html', {'trans_data': trans_data, 'input_data': input_data})
        elif 'gel-en' == request.POST['select-gel']:
            input_data = request.POST['trans']
            trans_data = GoogleTranslator(source='auto', target='en').translate(input_data)
            return render(request, 'translation/index.html', {'trans_data': trans_data, 'input_data': input_data})
        else:
            return render(request, "translation/index.html")
    else:
        return render(request, "translation/index.html")
