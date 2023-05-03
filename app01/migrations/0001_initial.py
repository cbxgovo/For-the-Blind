# Generated by Django 4.1.7 on 2023-04-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Iot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis', models.CharField(max_length=20)),
                ('waterdepth', models.FloatField(default=0.0, max_length=20)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]