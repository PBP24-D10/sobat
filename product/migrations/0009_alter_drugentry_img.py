# Generated by Django 5.1.2 on 2024-10-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_drugentry_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugentry',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]