# Generated by Django 3.2.7 on 2021-09-24 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0021_order_pending_or_dispatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pending_or_dispatched',
            field=models.BooleanField(default=False),
        ),
    ]