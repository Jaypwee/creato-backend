# Generated by Django 3.1.7 on 2021-04-29 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.UUID(
                    '0ffff299-f4f5-4f6d-8c42-1c696f728cbe'), max_length=64, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issueLimit', models.BigIntegerField(default=0)),
                ('subscribedAmount', models.PositiveBigIntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.UUID(
                    '80058122-d2b7-4539-b4ee-4c6c216dc801'), max_length=64, unique=True)),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('token', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.token')),
            ],
        ),
        migrations.CreateModel(
            name='CreatoUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('usdBalance', models.PositiveBigIntegerField(default=0)),
                ('balance', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='api.balance')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='token',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='api.token'),
        ),
    ]
