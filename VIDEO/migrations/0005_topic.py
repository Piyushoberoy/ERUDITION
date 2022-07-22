# Generated by Django 3.1.4 on 2022-06-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEO', '0004_auto_20220611_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=50)),
                ('topic_duration', models.FloatField()),
                ('topic_instructors_name', models.CharField(max_length=400)),
            ],
        ),
    ]
