# Generated by Django 5.1 on 2024-08-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('last_quarter_performance', models.FloatField()),
                ('daily_trading_volume', models.BigIntegerField()),
            ],
        ),
    ]
