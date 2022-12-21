from django.contrib import admin
from .models import Todo

# Register your models here.

# 管理画面で使用するモデルを登録する
admin.site.register(Todo)
