from django.urls import path
from itikaf import views as itikaf_views
from . import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('login/', itikaf_views.login_user, name='login'),
    path('search_mosques/', itikaf_views.search_mosques, name='search_mosques'),
    path('search_status/', itikaf_views.search_status, name='search_status'),
]