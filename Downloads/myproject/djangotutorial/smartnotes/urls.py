from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'smartnotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]