# Generated by Django 3.1.5 on 2021-02-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_mail_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
