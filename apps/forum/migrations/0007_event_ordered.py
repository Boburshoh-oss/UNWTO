# Generated by Django 4.2.5 on 2023-09-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_forum_short_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ordered',
            field=models.IntegerField(default=0),
        ),
    ]
