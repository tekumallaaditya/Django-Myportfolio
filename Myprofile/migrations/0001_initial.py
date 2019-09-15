# Generated by Django 2.2.4 on 2019-09-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(default=None)),
                ('start', models.DateField(default=None)),
                ('end', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='workexp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(default=None)),
                ('start', models.DateField(default=None)),
                ('end', models.DateField(default=None)),
            ],
        ),
    ]