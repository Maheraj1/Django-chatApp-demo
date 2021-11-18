from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<room_name>/', views.chat_room, name='chat_room'),
    path('r', views.goto_chat_room, name='get_room')
]
