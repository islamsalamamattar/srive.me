# Generated by Django 4.0.3 on 2022-04-24 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0028_alter_budget_frequency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category_type',
            options={'verbose_name_plural': 'Category Types'},
        ),
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
        migrations.AddField(
            model_name='budget',
            name='category_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.category_type'),
        ),
    ]
