# Generated by Django 3.0 on 2021-03-09 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210308_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagen',
            new_name='imagenp',
        ),
    ]
