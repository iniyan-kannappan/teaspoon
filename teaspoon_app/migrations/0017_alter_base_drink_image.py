# Generated by Django 3.2.7 on 2021-09-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0016_base_drink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_drink',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
