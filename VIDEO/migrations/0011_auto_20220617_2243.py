# Generated by Django 3.1.4 on 2022-06-17 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEO', '0010_auto_20220617_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Article',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='errors_and_omission',
            old_name='Error_and_Omission',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='jumbled_sentence',
            old_name='Jumbled_Sentence',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='parts_of_speech',
            old_name='Parts_Of_Speech',
            new_name='video',
        ),
    ]
