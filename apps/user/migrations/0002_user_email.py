# Generated by Django 4.2.5 on 2023-09-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
