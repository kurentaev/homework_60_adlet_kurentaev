# Generated by Django 4.1.1 on 2022-10-17 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_options_product_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_order', to='webapp.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product order',
                'verbose_name_plural': 'Product orders',
                'db_table': 'basket',
            },
        ),
    ]
