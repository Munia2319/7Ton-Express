<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-06-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_currency_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('recipient_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('house_number', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('apartment_number', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('product_details', models.CharField(max_length=1000)),
                ('delivery_type', models.CharField(max_length=200)),
                ('pickup_date_start', models.CharField(max_length=200)),
                ('pickup_date_end', models.CharField(max_length=200)),
                ('delivery_status', models.CharField(max_length=200)),
                ('estimated_weight', models.FloatField()),
                ('estimated_cost', models.FloatField()),
                ('volumetric_weight', models.FloatField()),
            ],
        ),
    ]
=======
# Generated by Django 4.0.5 on 2022-06-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_currency_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('recipient_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('house_number', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('apartment_number', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('product_details', models.CharField(max_length=1000)),
                ('delivery_type', models.CharField(max_length=200)),
                ('pickup_date_start', models.CharField(max_length=200)),
                ('pickup_date_end', models.CharField(max_length=200)),
                ('delivery_status', models.CharField(max_length=200)),
                ('estimated_weight', models.FloatField()),
                ('estimated_cost', models.FloatField()),
                ('volumetric_weight', models.FloatField()),
            ],
        ),
    ]
>>>>>>> 3d89e68835facbecfce5429c0e3d265323376159
