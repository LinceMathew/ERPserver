# Generated by Django 4.1.7 on 2023-04-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0011_rename_add_or_cosumed_stock_log_add_or_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_log',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock_log',
            name='gnr_no',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='stock_log',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock_log',
            name='snr_no',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
