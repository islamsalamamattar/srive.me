# Generated by Django 4.0.3 on 2022-04-23 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0026_remove_subscription_category_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_budget', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')], max_length=3, verbose_name='Currency')),
                ('frequency', models.CharField(choices=[('1', 'Daily'), ('7', 'Weekly'), ('30', 'Monthly')], max_length=12, verbose_name='Due')),
                ('deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]