# Generated by Django 3.2 on 2021-04-25 10:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0006_rename_url_modelno_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='Electronic/Products/')),
                ('img2', models.ImageField(upload_to='Electronic/Products/')),
                ('img3', models.ImageField(upload_to='Electronic/Products/')),
                ('ModelNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Electronics.modelno', verbose_name='Model No')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Electronics.brands')),
            ],
        ),
    ]
