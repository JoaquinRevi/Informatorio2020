# Generated by Django 3.0 on 2021-03-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210310_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagenp',
            field=models.ImageField(default='', upload_to='postmedia'),
            preserve_default=False,
        ),
    ]