# Generated by Django 3.2.6 on 2022-12-14 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
