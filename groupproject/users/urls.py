from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from users import views

app_name = 'users'

urlpatterns = [
  path('login', views.login_view, name='login'),
  path('logout', views.logout_view, name='logout'),
  path('registration', views.registration_view, name='registration'),
  path('dashboard', views.dashboard_view, name='dashboard'),
  path('bmi_calculator', views.bmi_calculator_view, name='bmi_calculator'),
  path('articles', views.articles_view, name='articles'),
  path('my_calories', views.my_calories_view, name='my_calories'),
  path('change_password', views.change_user_password_view, name='change_password'),
]