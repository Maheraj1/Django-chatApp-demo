import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage, ChatRoom
from .forms import ChatMessageForm, ChatMessage
from account.models import Account


class ChatRoomConsumer(AsyncWebsocketConsumer):
    connected = 0

    async def connect(self):
        self.connected += 1
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_user_name = 'chat_%s' % self.room_name + '_user_%s' % self.user.id
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_add(
            self.room_group_user_name,
            self.channel_name
        )
        await self.accept()
        messages = await self.get_messages()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'connected_message',
                'user': self.user.username,
            }
        )
        await self.channel_layer.group_send(
            self.room_group_user_name,
            {
                'type': 'connected_message',
                'users': self.user.username,
                'messages': messages,
            }
        )

    @database_sync_to_async
    def connect_user(self):
        return

    @database_sync_to_async
    def disconnect_user(self):
        return

    @database_sync_to_async
    def get_messages(self):
        list_msg = ''
        for messages in ChatMessage.objects.all():
            list_msg += (str(messages.by.username) + ': ' + str(messages.message) + '\n')
        print(list_msg)
        return list_msg

    @database_sync_to_async
    def send_message(self, message, user):
        form = ChatMessageForm({'message': message, 'by': user})
        print('filled')
        if form.is_valid():
            form.save()
            print('saved')

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        await self.send(text_data=json.dumps({'message': message, 'user': user}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_discard(
            self.room_group_user_name,
            self.channel_name
        )
        self.connected -= 1

    @database_sync_to_async
    def get_account(self, user):
        return Account.objects.get(username=user)

    async def connected_message(self, event):
        users = event.get('users')
        messages = event.get('messages')
        if users and messages:
            await self.send(text_data=json.dumps({"messages": messages, "users": users}))
        elif messages:
            await self.send(text_data=json.dumps({"messages": messages}))
        elif users:
            await self.send(text_data=json.dumps({'users': users}))

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        user = text_data_json.get('user')
        account = await self.get_account(user)
        await self.send_message(message, account)
        # all_messages = await self.get_messages()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        )
