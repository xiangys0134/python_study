# Generated by Django 2.1.14 on 2021-12-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
