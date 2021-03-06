# Generated by Django 3.2 on 2021-04-29 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmaceuticals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Medicines')),
            ],
            options={
                'verbose_name': 'Medicine',
                'db_table': 'medicine',
            },
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Medicine Name')),
                ('img', models.ImageField(upload_to='Product_Type_Images/')),
                ('url', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Medicine Type',
                'db_table': 'MedicineType',
            },
        ),
        migrations.CreateModel(
            name='pBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Brand Name')),
                ('img', models.ImageField(upload_to='Medicine/BrandName_Images/')),
                ('url', models.SlugField(blank=True, max_length=255, unique=True)),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmaceuticals.medicinetype')),
            ],
            options={
                'verbose_name': 'Brand',
                'db_table': 'pBrands',
            },
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.AddField(
            model_name='medicine',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmaceuticals.medicinetype'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmaceuticals.pbrands'),
        ),
    ]
