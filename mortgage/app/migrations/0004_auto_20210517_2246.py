# Generated by Django 3.2.1 on 2021-05-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_mortgage_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mortgage',
            name='interest_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mortgage',
            name='period',
            field=models.IntegerField(),
        ),
    ]
