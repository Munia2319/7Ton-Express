# Generated by Django 4.0.5 on 2022-08-25 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0020_delete_new_order_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order_info',
        ),
    ]
