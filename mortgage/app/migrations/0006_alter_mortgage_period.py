# Generated by Django 3.2.1 on 2021-05-30 20:00

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210519_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mortgage',
            name='period',
            field=models.IntegerField(validators=[app.models.positive_number, app.models.max_period]),
        ),
    ]
