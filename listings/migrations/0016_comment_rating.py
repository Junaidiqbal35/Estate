# Generated by Django 2.2.2 on 2019-07-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20190707_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='3'),
        ),
    ]
