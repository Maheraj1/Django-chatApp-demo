from django.urls import path
from . import views


urlpatterns = [
    path('edit/', views.settings, name='edit_account'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),
]
