# Generated by Django 2.2.2 on 2019-08-01 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20190801_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='listing',
        ),
    ]