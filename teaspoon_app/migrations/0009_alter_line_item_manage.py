# Generated by Django 3.2.7 on 2021-09-14 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teaspoon_app', '0008_line_item_manage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_item',
            name='manage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]