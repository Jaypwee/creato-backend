# Generated by Django 3.1.7 on 2021-04-29 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20210429_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creatouser',
            name='balance',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.balance'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='uuid',
            field=models.CharField(default=uuid.UUID('ccb47a8e-bfd7-41a6-b2ae-b7fe39624b73'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='uuid',
            field=models.CharField(default=uuid.UUID('430f7360-df15-40a6-9b7a-eb57d4c13219'), max_length=64, unique=True),
        ),
    ]
