# Generated by Django 5.1.1 on 2024-10-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_drugentry_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugentry',
            options={'ordering': ['name'], 'verbose_name_plural': 'Drug Entries'},
        ),
        migrations.AlterField(
            model_name='drugentry',
            name='image',
            field=models.ImageField(upload_to='drugs/'),
        ),
    ]
