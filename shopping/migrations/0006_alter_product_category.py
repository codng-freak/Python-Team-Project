# Generated by Django 3.2.3 on 2021-05-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_remove_product_prod_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='UW', max_length=15),
        ),
    ]
