# Generated by Django 4.2.8 on 2023-12-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_ourgallery_img_large_ourgallery_img_small_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourgallery',
            name='img_small',
        ),
        migrations.AddField(
            model_name='ourgallery',
            name='img_large',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Large Image'),
        ),
        migrations.AlterField(
            model_name='ourgallery',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Small Image'),
        ),
    ]
