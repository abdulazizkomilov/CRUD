# Generated by Django 4.0.3 on 2022-03-20 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
