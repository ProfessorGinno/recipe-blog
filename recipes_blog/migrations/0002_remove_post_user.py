# Generated by Django 4.2.4 on 2023-08-18 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
