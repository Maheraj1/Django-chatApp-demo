# Generated by Django 3.1.5 on 2021-02-15 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='unread',
        ),
    ]
