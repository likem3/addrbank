# Generated by Django 4.2.3 on 2023-07-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phrase',
            field=models.TextField(blank=True, help_text='wallet pharse', null=True),
        ),
    ]
