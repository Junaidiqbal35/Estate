# Generated by Django 2.2.2 on 2019-06-25 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0002_auto_20190428_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='host_id',
        ),
        migrations.AddField(
            model_name='listing',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]