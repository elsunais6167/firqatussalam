from django.urls import path
from . import views

urlpatterns = [
    #path('masjids/<int:city_id>/', views.home, name='masjids_by_city'),
    path('', views.home, name='home'),
    path('applyi', views.apply, name='applyi'),
]