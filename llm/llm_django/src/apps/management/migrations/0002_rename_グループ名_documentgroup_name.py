# Generated by Django 5.0.3 on 2024-03-17 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentgroup',
            old_name='グループ名',
            new_name='name',
        ),
    ]
