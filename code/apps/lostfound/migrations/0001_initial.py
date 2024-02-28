# Generated by Django 2.1 on 2018-12-24 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(default='img/default.jpg', upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='LostfoundPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('失物招领', '失物招领'), ('寻物启事', '寻物启事')], default=0, max_length=10)),
                ('location', models.CharField(choices=[('望江', '望江'), ('江安', '江安'), ('华西', '华西')], default=0, max_length=100)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('objecttime', models.CharField(blank=True, max_length=500)),
                ('details', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
