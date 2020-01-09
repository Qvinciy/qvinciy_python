# Generated by Django 3.0.2 on 2020-01-08 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('vk', models.CharField(max_length=200)),
                ('insta', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
                ('avatarka', models.ImageField(upload_to='')),
                ('filename', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('reiting', models.IntegerField()),
            ],
        ),
    ]
