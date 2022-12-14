# Generated by Django 4.1.1 on 2022-10-16 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_productslist_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200, verbose_name='Image'),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
