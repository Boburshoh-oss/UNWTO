# Generated by Django 4.2.5 on 2023-09-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='org_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
