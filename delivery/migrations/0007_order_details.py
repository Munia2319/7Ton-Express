# Generated by Django 4.0 on 2022-06-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_delete_order_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
