# Generated by Django 5.0.4 on 2024-07-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_first_name_item_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='first_name',
        ),
    ]
