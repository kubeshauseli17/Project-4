# Generated by Django 3.2.6 on 2022-10-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('mod', 'mod'), ('type', 'type')], max_length=100),
        ),
    ]
