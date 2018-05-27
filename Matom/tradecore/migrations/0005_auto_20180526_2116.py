# Generated by Django 2.0.5 on 2018-05-27 01:16

from django.db import migrations, models
import django.db.models.deletion
import tradecore.models


class Migration(migrations.Migration):

    dependencies = [
        ('tradecore', '0004_auto_20180526_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemstack',
            name='location',
        ),
        migrations.AlterField(
            model_name='factory',
            name='storage',
            field=models.OneToOneField(default=tradecore.models.InventoryManager.create_inventory, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tradecore.Inventory'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inventory',
            field=models.OneToOneField(default=tradecore.models.InventoryManager.create_inventory, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tradecore.Inventory'),
        ),
        migrations.AlterField(
            model_name='traderequest',
            name='offered_items',
            field=models.OneToOneField(default=tradecore.models.InventoryManager.create_inventory, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tradecore.Inventory'),
        ),
        migrations.AlterField(
            model_name='traderequest',
            name='requested_items',
            field=models.OneToOneField(default=tradecore.models.InventoryManager.create_inventory, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tradecore.Inventory'),
        ),
    ]