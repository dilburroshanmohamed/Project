# Generated by Django 4.2.6 on 2024-01-27 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_rename_awardtype_award_chessnumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='groups',
            new_name='GROUPS',
        ),
    ]
