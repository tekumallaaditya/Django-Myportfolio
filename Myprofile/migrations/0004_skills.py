# Generated by Django 2.2.4 on 2019-09-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myprofile', '0003_auto_20190914_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
            ],
        ),
    ]
