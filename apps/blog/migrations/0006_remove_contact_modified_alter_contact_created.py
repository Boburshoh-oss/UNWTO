# Generated by Django 4.2.5 on 2023-09-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact_title_en_contact_title_ru_contact_title_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='modified',
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
