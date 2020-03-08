from django.urls import path

from . import views

urlpatterns = [
  path('', views.ApiIndex, name='index'),
  path('get/', views.methodGet, name='get'),
  path('post/', views.methodPost, name='post'),
  path('put/', views.methodPut, name='put'),
  path('delete/', views.methodDelete, name='delete'),
]
