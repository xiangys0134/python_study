# Generated by Django 2.1.1 on 2019-01-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20190103_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(db_table='book2authors', to='app01.Author'),
        ),
    ]
