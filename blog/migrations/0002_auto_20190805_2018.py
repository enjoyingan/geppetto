# Generated by Django 2.2.3 on 2019-08-05 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='phone',
        ),
    ]
