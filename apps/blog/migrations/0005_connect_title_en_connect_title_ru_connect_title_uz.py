# Generated by Django 4.2.5 on 2023-09-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_connect'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]