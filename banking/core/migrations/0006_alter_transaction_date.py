# Generated by Django 3.2.13 on 2022-06-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='2022-06-13 10:00:00'),
        ),
    ]
