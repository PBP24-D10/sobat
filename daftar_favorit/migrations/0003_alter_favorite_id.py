# Generated by Django 5.1 on 2024-10-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_favorit', '0002_alter_favorite_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
