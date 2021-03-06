# Generated by Django 3.1.7 on 2021-04-30 04:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210430_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='id',
        ),
        migrations.AddField(
            model_name='token',
            name='isIssued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='isListed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='uuid',
            field=models.CharField(
                default=uuid.UUID('cc4bb57a-5813-4e69-bf5f-e88b8ccce527'),
                max_length=64,
                primary_key=True,
                serialize=False,
                unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='uuid',
            field=models.CharField(
                default=uuid.UUID('eb78c0d8-f05a-4062-aa6b-04e92f03e1bb'),
                max_length=64,
                unique=True),
        ),
    ]
