# Generated by Django 2.2.6 on 2019-10-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16)),
                ('u_age', models.IntegerField(default=1)),
                ('u_addr', models.CharField(max_length=16)),
            ],
        ),
    ]