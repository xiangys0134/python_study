# Generated by Django 2.1.14 on 2021-12-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_heroinfo_isdelete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
