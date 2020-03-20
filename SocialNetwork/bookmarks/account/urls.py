from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    re_path('^login/$', auth_views.LoginView.as_view(), name="login"),
    re_path('^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    path('', views.dashboard, name='dashboard')
]
