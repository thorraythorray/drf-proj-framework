# Generated by Django 4.2.6 on 2023-10-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_tm', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('test', models.CharField(max_length=64, verbose_name='test')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
