# Generated by Django 3.0.4 on 2020-04-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200401_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadavre',
            name='code',
            field=models.SlugField(help_text='Introduce un código secreto', max_length=200, unique=True, verbose_name='Código'),
        ),
    ]
