# Generated by Django 5.0.1 on 2025-04-10 10:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_api', '0003_alter_customuser_referral_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
