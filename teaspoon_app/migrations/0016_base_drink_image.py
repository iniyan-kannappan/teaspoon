# Generated by Django 3.2.7 on 2021-09-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0015_line_item_toppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='base_drink',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
