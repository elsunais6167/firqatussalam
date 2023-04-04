from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.loggingout, name='logout'),
    path('applyi/<str:pk>/', views.apply, name='applyi'),
    path('form', views.application, name='form'),
    path('update_info/<int:pk>/', views.update_info, name='update_info'),
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
    path('state_admin/', views.state_admin, name='state_admin'),
    path('add_mosque/', views.add_mosque, name='add_mosque'),
    path('assign_admin/<str:pk>/', views.assign_admin, name='assign_admin' ),
    path('admin_list/', views.listUsers, name='admin_list'),
    path('action/', views.action, name='action'),
    path('action_info/<int:pk>/', views.action_info, name='action_info'),
    path('id_card/<int:pk>/', views.id_card, name='id_card'),
    
]