# Generated by Django 2.1.1 on 2019-04-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0008_auto_20190501_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='86A44E01016D', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADD94E986AFF', max_length=14),
        ),
    ]
