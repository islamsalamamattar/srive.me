# Generated by Django 3.2.5 on 2022-03-05 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_auto_20220305_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.store'),
        ),
    ]
