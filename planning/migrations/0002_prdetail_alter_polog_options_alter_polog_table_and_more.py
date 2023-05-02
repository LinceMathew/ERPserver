# Generated by Django 4.1.7 on 2023-05-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prdetail',
            fields=[
                ('srlno', models.BigAutoField(primary_key=True, serialize=False)),
                ('prno', models.BigIntegerField(blank=True, null=True)),
                ('pono', models.CharField(blank=True, max_length=10, null=True)),
                ('pryear', models.CharField(blank=True, max_length=4, null=True)),
                ('matcode', models.CharField(blank=True, max_length=6, null=True)),
                ('ssrl', models.CharField(blank=True, max_length=2, null=True)),
                ('submited', models.BooleanField(blank=True, null=True)),
                ('pr_qty', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('pr_date', models.DateField(blank=True, null=True)),
                ('rq_date', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=20, null=True)),
                ('podate', models.DateField(blank=True, null=True)),
                ('poqty', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('supcode', models.CharField(blank=True, max_length=20, null=True)),
                ('porate', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('lpr', models.CharField(blank=True, max_length=10, null=True)),
                ('lprdt', models.DateField(blank=True, null=True)),
                ('pr_pen', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('stock', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('tpndr', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr1', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr2', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr3', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr4', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr5', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr6', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr7', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr8', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr9', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr10', models.CharField(blank=True, max_length=20, null=True)),
                ('pndpo', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('ratehike', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('sugg', models.CharField(blank=True, max_length=25, null=True)),
                ('wor1', models.CharField(blank=True, max_length=10, null=True)),
                ('wor2', models.CharField(blank=True, max_length=10, null=True)),
                ('wor3', models.CharField(blank=True, max_length=10, null=True)),
                ('wor4', models.CharField(blank=True, max_length=10, null=True)),
                ('wor5', models.CharField(blank=True, max_length=10, null=True)),
                ('wo5r', models.CharField(blank=True, max_length=10, null=True)),
                ('prremark', models.CharField(blank=True, max_length=250, null=True)),
                ('itremark', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'prdetail',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='polog',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='polog',
            table='polog',
        ),
        migrations.CreateModel(
            name='Prdetaillog',
            fields=[
                ('slno', models.BigAutoField(primary_key=True, serialize=False)),
                ('srlno', models.IntegerField(blank=True, null=True)),
                ('prno', models.BigIntegerField(blank=True, null=True)),
                ('pono', models.CharField(blank=True, max_length=10, null=True)),
                ('pryear', models.CharField(blank=True, max_length=4, null=True)),
                ('matcode', models.CharField(blank=True, max_length=6, null=True)),
                ('ssrl', models.CharField(blank=True, max_length=2, null=True)),
                ('submited', models.BooleanField(blank=True, null=True)),
                ('pr_qty', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('pr_date', models.DateField(blank=True, null=True)),
                ('rq_date', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=20, null=True)),
                ('podate', models.DateField(blank=True, null=True)),
                ('poqty', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('supcode', models.CharField(blank=True, max_length=20, null=True)),
                ('porate', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('lpr', models.CharField(blank=True, max_length=10, null=True)),
                ('lprdt', models.DateField(blank=True, null=True)),
                ('pr_pen', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('stock', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('tpndr', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr1', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr2', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr3', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr4', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr5', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr6', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr7', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr8', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr9', models.CharField(blank=True, max_length=20, null=True)),
                ('apprsr10', models.CharField(blank=True, max_length=20, null=True)),
                ('pndpo', models.DecimalField(blank=True, decimal_places=3, max_digits=17, null=True)),
                ('ratehike', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('sugg', models.CharField(blank=True, max_length=25, null=True)),
                ('wor1', models.CharField(blank=True, max_length=10, null=True)),
                ('wor2', models.CharField(blank=True, max_length=10, null=True)),
                ('wor3', models.CharField(blank=True, max_length=10, null=True)),
                ('wor4', models.CharField(blank=True, max_length=10, null=True)),
                ('wor5', models.CharField(blank=True, max_length=10, null=True)),
                ('wo5r', models.CharField(blank=True, max_length=10, null=True)),
                ('prremark', models.CharField(blank=True, max_length=250, null=True)),
                ('itremark', models.CharField(blank=True, max_length=50, null=True)),
                ('logid', models.CharField(blank=True, max_length=25, null=True)),
                ('eddt', models.DateField(blank=True, null=True)),
                ('edtime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prdetaillog',
                'managed': True,
                'unique_together': {('slno', 'srlno')},
            },
        ),
    ]
