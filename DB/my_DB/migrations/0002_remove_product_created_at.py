# Generated by Django 5.0.8 on 2024-08-11 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_DB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
    ]