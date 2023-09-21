from django.urls import path
from . import views

app_name = 'server'

urlpatterns = [
    path('test/', views.testapp_index, name='testapp_index'),
    path('KcBERT/', views.KcBERT_result, name='KcBERT_index'),
    path('post/', views.post_view, name='post_index'),
    path('parameter', views.post_test, name='parameter'),
]