# Generated by Django 5.0.3 on 2024-05-02 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserRegister',
        ),
    ]
