from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>hello world</h1>')

# ホーム画面
class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'   # HTMLに表示する時の変数名

# 詳細画面
class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'
    
# 作成画面
class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'      # カラムの全選択
    success_url = reverse_lazy('list')      # 'list'という名前がついたページに遷移する

# 編集画面
class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

# 削除画面
class TodoDelete(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('list')
    
