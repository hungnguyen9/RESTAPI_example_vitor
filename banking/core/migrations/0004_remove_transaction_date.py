# Generated by Django 3.2.13 on 2022-06-13 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
    ]
