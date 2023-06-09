from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import openai

# Create your views here.

openai.api_key = '***'


def index(request): 
    if request.method == 'POST':
        input_data = request.POST['chatai']
        def ask_gpt(prompt):
            res = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}])
            
            return res.choices[0]['message']['content']
        
        chat_data = ask_gpt(input_data)
        
        return render(request, 'translation/index.html', {'chat_data': chat_data})
    else:
        return render(request, "translation/index.html")
