# Generated by Django 2.1.14 on 2020-02-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('coment_num', models.IntegerField()),
                ('poll_num', models.IntegerField()),
            ],
        ),
    ]
