# Generated by Django 2.2.10 on 2022-03-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0012_auto_20220313_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='card',
            field=models.BooleanField(default=False),
        ),
    ]
