# Generated by Django 2.1.7 on 2019-04-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0011_auto_20190501_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='FA667647731D', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADD43D89F703', max_length=14),
        ),
    ]
