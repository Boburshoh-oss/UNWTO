# Generated by Django 4.2.5 on 2023-09-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inivitation',
            name='code',
            field=models.CharField(unique=True),
        ),
    ]
