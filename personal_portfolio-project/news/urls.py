from django.urls import path,include
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.News, name='News' ),

]
