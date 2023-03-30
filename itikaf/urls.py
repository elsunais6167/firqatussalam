from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applyi/<str:pk>/', views.apply, name='applyi'),
    path('form', views.application, name='form'),
    path('mosque_dashboard', views.mosque_dashboard, name='mosque_dashboard'),
    path('new_applicant', views.new_applicant, name='new_applicant'),
    path('profile', views.profile, name='profile'),
    path('applicant_info/<int:pk>/', views.applicant_info, name='applicant_info'),
    path('printout', views.printout, name='printout'),
    path('comment/<str:pk>/', views.comment, name='comment'),
    path('approved/<int:pk>/', views.approved, name='approved'),
    path('checkin/<str:pk>/', views.checkin, name='checkin'),
    path('checkout/<str:pk>/', views.checkout, name='checkout'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out, name='logout'),
]