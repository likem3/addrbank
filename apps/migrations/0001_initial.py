# Generated by Django 4.2.3 on 2023-07-04 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='updated datetime')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='deleted datetime', null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('nonactive', 'Nonactive')], help_text='status of data availability', max_length=20)),
                ('name', models.CharField(help_text='name of the currency such as bitcoin, ethereum, tron, etc.', max_length=20)),
                ('symbol', models.CharField(help_text='symbol of the currency such as BTC, ETH, TRX, etc.', max_length=10)),
                ('blockchain', models.CharField(help_text='blochain name of the currency such as bitcoin, etherum, tron, etc.', max_length=50)),
                ('std', models.CharField(blank=True, help_text='standard token of the currency ex ERC20, TRC20, BEP20, etc.', max_length=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user performing create action', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'apps_currencies',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='updated datetime')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='deleted datetime', null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('nonactive', 'Nonactive')], help_text='status of data availability', max_length=20)),
                ('address', models.CharField(help_text='unique currency address', max_length=255, unique=True)),
                ('phrase', models.TextField(help_text='wallet pharse')),
                ('resource', models.TextField(help_text='resource app of the wallet or url')),
                ('created_by', models.ForeignKey(blank=True, help_text='user performing create action', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(help_text='cryptocurrency of the address', on_delete=django.db.models.deletion.CASCADE, related_name='address', to='apps.currency')),
            ],
            options={
                'db_table': 'apps_addresses',
            },
        ),
    ]