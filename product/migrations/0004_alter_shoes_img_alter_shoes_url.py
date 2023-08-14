# Generated by Django 4.2.1 on 2023-08-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_shoes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='img',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='url',
            field=models.CharField(max_length=350, unique=True),
        ),
    ]