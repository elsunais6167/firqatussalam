from django.urls import path
from . import views

urlpatterns = [
    #path('masjids/<int:city_id>/', views.home, name='masjids_by_city'),
    path('', views.home, name='home'),
    path('applyi/<str:pk>/', views.apply, name='applyi'),
    path('form', views.application, name='form'),
    path('dashboard', views.dashboard, name='dashboard')
]