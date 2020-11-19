# Generated by Django 3.0.7 on 2020-11-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, verbose_name='用户名')),
                ('passworld', models.CharField(max_length=20, verbose_name='密码')),
                ('iphone', models.CharField(max_length=11, verbose_name='手机号')),
                ('level', models.CharField(default='visitors', max_length=11, verbose_name='权限')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
