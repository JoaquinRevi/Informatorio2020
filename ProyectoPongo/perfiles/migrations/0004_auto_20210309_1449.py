# Generated by Django 3.0 on 2021-03-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_auto_20210309_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='http://assets.stickpng.com/images/585e4beacb11b227491c3399.png', upload_to='perfilesmedia'),
        ),
    ]
