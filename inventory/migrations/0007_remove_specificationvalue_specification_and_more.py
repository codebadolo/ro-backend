# Generated by Django 5.1.7 on 2025-03-22 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specificationvalue',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='specification',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='specification',
            name='description',
        ),
        migrations.RemoveField(
            model_name='specification',
            name='name',
        ),
        migrations.AddField(
            model_name='specification',
            name='key',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='specification',
            name='value',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.CreateModel(
            name='SpecificationGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification_groups', to='inventory.product')),
            ],
        ),
        migrations.AddField(
            model_name='specification',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='inventory.specificationgroup'),
        ),
        migrations.DeleteModel(
            name='ProductSpecification',
        ),
        migrations.DeleteModel(
            name='SpecificationValue',
        ),
    ]
