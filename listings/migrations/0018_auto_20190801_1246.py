# Generated by Django 2.2.2 on 2019-08-01 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_auto_20190731_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='listings.Listing'),
        ),
    ]
