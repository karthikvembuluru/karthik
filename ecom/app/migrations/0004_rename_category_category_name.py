# Generated by Django 5.0.3 on 2024-05-08 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_name_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]