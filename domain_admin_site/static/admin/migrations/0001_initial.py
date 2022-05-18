# Generated by Django 2.1.4 on 2022-05-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
                ('port', models.IntegerField(default=443)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'domaininfo',
            },
        ),
    ]
