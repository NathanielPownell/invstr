# Generated by Django 3.2 on 2021-04-20 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_account_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='avatar',
        ),
    ]
