# Generated by Django 2.1.4 on 2019-12-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=32)),
                ('publish', models.CharField(max_length=32)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]