# Generated by Django 5.1 on 2024-10-25 03:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_favorit', '0007_remove_favorite_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
