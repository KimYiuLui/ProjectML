# Generated by Django 2.2.2 on 2019-06-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190613_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated',
        ),
    ]
