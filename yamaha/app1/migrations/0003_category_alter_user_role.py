# Generated by Django 5.0.3 on 2024-04-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('users', 'Users'), ('dealer', 'Dealer'), ('admin', 'Admin')], default='users', max_length=20),
        ),
    ]
