# Generated by Django 2.2.4 on 2019-09-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='introPageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_intro', models.CharField(max_length=200)),
                ('main_into', models.TextField()),
                ('main_pic', models.ImageField(upload_to='images/')),
            ],
        ),
    ]