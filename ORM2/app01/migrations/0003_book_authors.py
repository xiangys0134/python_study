# Generated by Django 2.1.1 on 2019-01-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app01.Author'),
        ),
    ]
