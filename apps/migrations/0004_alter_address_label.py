# Generated by Django 4.2.3 on 2023-07-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_address_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='label',
            field=models.CharField(blank=True, help_text='remark for the address', max_length=255, null=True),
        ),
    ]
