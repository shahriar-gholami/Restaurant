# Generated by Django 4.2.8 on 2024-04-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orderitem_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
