# Generated by Django 3.2.7 on 2021-09-15 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0011_auto_20210915_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_item',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teaspoon_app.order'),
        ),
    ]