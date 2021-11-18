from django.shortcuts import render, redirect
from .forms import ChatRoomForm, ChatRoom
from account.models import Account


def index(request):
    context = {}
    print(ChatRoom.objects.all())
    return render(request, 'home.html', context)


def chat_room(request, room_name):
    context = {'room_name': room_name}
    print(Account.objects.all())
    if request.user.is_authenticated:
        if room_name in ChatRoom.objects.values_list('name', flat=True):
            return render(request, 'room.html', context)
        else:
            print('Creating new room......')
            form = ChatRoomForm({'name': room_name, 'max_users': 122})
            if form.is_valid():
                form.save()
                print('Created New room')
            return render(request, 'room.html', context)
    return redirect('login')


def goto_chat_room(request):
    room_name = request.GET.get('room_name')
    if request.user.is_authenticated:
        if room_name in ChatRoom.objects.values_list('name', flat=True):
            return redirect('chat_room', room_name)
        else:
            print('Creating new room......')
            form = ChatRoomForm({'name': room_name, 'max_users': 122})
            if form.is_valid():
                form.save()
                print('Created New room')
        return redirect('chat_room', room_name)
    return redirect('login')
