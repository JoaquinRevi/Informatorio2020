# Generated by Django 3.0 on 2021-03-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_auto_20210309_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(upload_to='perfilesmedia'),
        ),
    ]
