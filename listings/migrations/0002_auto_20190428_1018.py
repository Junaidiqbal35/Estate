# Generated by Django 2.1.2 on 2019-04-28 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='host_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='host.Host'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
    ]
