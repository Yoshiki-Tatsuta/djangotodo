from django.urls import path
from . import views
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    # path('', views.index),
    path('', TodoList.as_view(), name='list'),  # ホーム画面
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),   # 詳細画面
    path('create/', TodoCreate.as_view(), name='create'),   # 作成画面
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),   # 編集画面
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),   # 削除画面
]
