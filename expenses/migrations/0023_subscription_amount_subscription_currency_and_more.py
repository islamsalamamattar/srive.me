# Generated by Django 4.0.3 on 2022-04-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0022_expense_type_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='amount',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='currency',
            field=models.CharField(choices=[('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')], default='EGP', max_length=3, verbose_name='Currency'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='type',
            field=models.CharField(choices=[('S', 'Subsription'), ('I', 'Installment')], max_length=12, verbose_name='subcription/installment'),
        ),
    ]