# Generated by Django 3.2.7 on 2021-09-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0019_remove_line_item_toppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='line_item',
            name='toppings',
            field=models.ManyToManyField(to='teaspoon_app.topping'),
        ),
        migrations.DeleteModel(
            name='line_item_topping',
        ),
    ]
