# Generated by Django 3.2.3 on 2021-07-10 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0002_rename_name_account_detail_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='deadline_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]