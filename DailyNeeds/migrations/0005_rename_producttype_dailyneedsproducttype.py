# Generated by Django 3.2 on 2021-05-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DailyNeeds', '0004_auto_20210429_0038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductType',
            new_name='DailyNeedsProductType',
        ),
    ]
