# Generated by Django 2.2.2 on 2019-08-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0022_auto_20190801_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=4),
        ),
    ]
