# Generated by Django 2.1.1 on 2019-01-07 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20190104_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=32)),
            ],
        ),
    ]
