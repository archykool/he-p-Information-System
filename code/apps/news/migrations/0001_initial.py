# Generated by Django 2.0.2 on 2018-12-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qingchunnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'qingchun_news',
            },
        ),
        migrations.CreateModel(
            name='TestScrapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('source', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'test_scrapy',
            },
        ),
        migrations.CreateModel(
            name='Xuegongnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'xuegong_news',
            },
        ),
    ]
