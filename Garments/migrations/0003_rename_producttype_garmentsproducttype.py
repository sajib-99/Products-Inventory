# Generated by Django 3.2 on 2021-05-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Garments', '0002_brandsname_productdetail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductType',
            new_name='GarmentsProductType',
        ),
    ]
