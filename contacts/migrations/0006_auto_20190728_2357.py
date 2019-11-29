# Generated by Django 2.2.2 on 2019-07-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='host_photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='listing_photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
