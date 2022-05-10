from django.urls import path,include
from app_users.views import login_view


app_name = 'app_users'

urlpatterns = [
    path('login', login_view, name='login' ),

]
