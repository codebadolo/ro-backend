# Generated by Django 5.1.7 on 2025-03-22 03:39

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_productinventory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinventory',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
