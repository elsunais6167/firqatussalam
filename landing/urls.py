from django.urls import path
from itikaf import views as itikaf_views
from . import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('login/', itikaf_views.login_user, name='login'),
    
]