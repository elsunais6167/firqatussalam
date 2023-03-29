from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applyi/<str:pk>/', views.apply, name='applyi'),
    path('form', views.application, name='form'),
    path('mosque_dashboard', views.mosque_dashboard, name='mosque_dashboard'),
    path('new_applicant', views.new_applicant, name='new_applicant'),
    path('profile', views.profile, name='profile'),
    path('applicant_info/<str:pk>/', views.applicant_info, name='applicant_info'),
    path('printout', views.printout, name='printout'),
]