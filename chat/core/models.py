from django.db import models


class ChatMessage(models.Model):
    message = models.TextField()
    by = models.ForeignKey('account.Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class ChatRoom(models.Model):
    name = models.CharField(max_length=2000)
    max_users = models.IntegerField(default=100)

    def __str__(self):
        return self.name
