# Generated by Django 3.2.5 on 2021-07-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
