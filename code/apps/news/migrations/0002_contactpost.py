# Generated by Django 2.1 on 2018-12-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]