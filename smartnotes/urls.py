from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'smartnotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='smartnotes:login'), name='logout'),
    path('register/', views.register, name='register'),
]
