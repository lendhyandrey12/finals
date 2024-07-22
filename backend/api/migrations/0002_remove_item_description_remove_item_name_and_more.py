# Generated by Django 5.0.4 on 2024-07-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='item',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='middle_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
