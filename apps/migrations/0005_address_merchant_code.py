# Generated by Django 4.2.3 on 2023-07-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_address_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='merchant_code',
            field=models.PositiveIntegerField(blank=True, help_text='merchant code use the address', null=True),
        ),
    ]
