from django import forms
from .models import ChatMessage, ChatRoom


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('message', 'by')


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('name', 'max_users')
