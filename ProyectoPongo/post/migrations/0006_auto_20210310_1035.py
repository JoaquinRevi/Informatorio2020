# Generated by Django 3.0 on 2021-03-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210309_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagenp',
            field=models.ImageField(blank=True, null=True, upload_to='postmedia'),
        ),
    ]