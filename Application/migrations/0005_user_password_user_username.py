# Generated by Django 5.1.1 on 2024-10-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0004_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]