# Generated by Django 4.2.5 on 2023-09-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_inivitation_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
