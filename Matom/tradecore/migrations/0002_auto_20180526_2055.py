# Generated by Django 2.0.5 on 2018-05-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradecore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
