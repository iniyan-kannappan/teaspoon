# Generated by Django 3.2.7 on 2021-09-11 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaspoon_app', '0002_auto_20210909_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.IntegerField()),
                ('address', models.CharField(max_length=191)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='products_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='order_drink',
            name='drink_id',
        ),
        migrations.RemoveField(
            model_name='order_drink',
            name='topping_id',
        ),
        migrations.DeleteModel(
            name='base_drink',
        ),
        migrations.DeleteModel(
            name='order_drink',
        ),
        migrations.DeleteModel(
            name='topping',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaspoon_app.order'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaspoon_app.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teaspoon_app.product'),
        ),
    ]
