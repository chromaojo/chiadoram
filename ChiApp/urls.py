from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('about', views.about, name='about'),
    path('read/<str:pk>', views.read, name='read'),
    path('deleteMessage/<int:pk>', views.deleteMessage, name='deleteMessage'),
    path('customer', views.customer, name='customer'),
]