# Generated by Django 5.1.1 on 2024-10-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_age_range_drugentry_availibility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugentry',
            name='availibility',
            field=models.BooleanField(default=True),
        ),
    ]