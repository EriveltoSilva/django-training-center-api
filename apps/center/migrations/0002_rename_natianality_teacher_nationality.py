# Generated by Django 5.0.1 on 2024-02-06 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='natianality',
            new_name='nationality',
        ),
    ]