# Generated by Django 3.2.7 on 2021-09-16 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0012_alter_line_item_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]