# Generated by Django 3.0 on 2021-03-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_auto_20210309_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='/perfiles/static/img/defaultperfil.jpg', upload_to='perfilesmedia'),
        ),
    ]
