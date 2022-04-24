# Generated by Django 4.0.3 on 2022-04-18 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0021_rename_store_expense_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='type',
            field=models.CharField(choices=[('S', 'Subsription'), ('I', 'Installment'), ('E', 'Expense')], default='E', max_length=12, verbose_name='Type'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('S', 'Subsription'), ('I', 'Installment')], max_length=12, verbose_name='subscription/installment')),
                ('frequency', models.CharField(choices=[('1', 'Monthly'), ('3', 'Quarterly'), ('12', 'Yearly')], max_length=12, verbose_name='Due')),
                ('next_due', models.DateField()),
                ('autopay', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.category_type')),
            ],
        ),
    ]
