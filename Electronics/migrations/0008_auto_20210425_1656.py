# Generated by Django 3.2 on 2021-04-25 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0007_productdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdetails',
            options={'verbose_name': 'Product Detail'},
        ),
        migrations.AlterModelTable(
            name='productdetails',
            table='ProductDetails',
        ),
    ]
