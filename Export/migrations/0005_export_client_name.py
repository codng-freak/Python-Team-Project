# Generated by Django 3.2.3 on 2021-06-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Export', '0004_client_demand_client_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='client_name',
            field=models.CharField(default='Default', max_length=50),
            preserve_default=False,
        ),
    ]
