# Generated by Django 5.0.3 on 2024-05-08 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='Category',
        ),
    ]
