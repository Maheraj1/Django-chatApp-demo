# Generated by Django 3.1.5 on 2021-02-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210211_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=100)),
                ('by', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('unread', models.BooleanField(default=True, null=True)),
                ('file', models.FileField(upload_to='data/mail/files')),
            ],
        ),
    ]
