# Generated by Django 3.2.8 on 2021-10-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0010_userhastodolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='author',
        ),
    ]
