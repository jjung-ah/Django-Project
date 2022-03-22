from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('content/create/<int:user_id>/', views.content_create, name='content_create'),
    path('user/create/', views.user_create, name='user_create'),
]