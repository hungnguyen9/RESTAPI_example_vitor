# Generated by Django 3.2.13 on 2022-06-13 02:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 2, 53, 24, 606431, tzinfo=utc)),
        ),
    ]
