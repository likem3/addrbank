# Generated by Django 4.2.3 on 2023-07-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_address_is_used_address_label_address_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='delete data status'),
        ),
        migrations.AddField(
            model_name='currency',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='delete data status'),
        ),
    ]