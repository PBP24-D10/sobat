# Generated by Django 5.1 on 2024-10-24 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_favorit', '0004_alter_favorite_id'),
        ('product', '0005_alter_drugentry_availibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.drugentry'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
