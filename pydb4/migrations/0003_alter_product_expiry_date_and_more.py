# Generated by Django 4.2.1 on 2023-06-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pydb4', '0002_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_on_hand',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_on_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='N/A', max_length=60),
        ),
    ]
