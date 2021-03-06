# Generated by Django 2.1.14 on 2020-02-07 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name': '出版社'},
        ),
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Publish', verbose_name='出版社'),
        ),
    ]
