from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers
import datetime

class ItemType(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class InventoryManager(models.Manager):
    def create_inventory(self):
        return self.create()

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    objects = InventoryManager()

def new_inventory():
    return Inventory.objects.create_inventory().id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="+", default=new_inventory)
    luxury = models.IntegerField(default=0)
    reputation = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except AttributeError:
        Profile.objects.create(user=instance)
        instance.profile.save()

class ItemStack(models.Model):
    location = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="items")
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.quantity) + " " + str(self.itemtype)

class Factory(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    storage = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="+", default=new_inventory)
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class TradeRequest(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="outgoing_requests")
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="incoming_requests")
    accepted = models.BooleanField(default=False)
    requested_items = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="+", default=new_inventory)
    offered_items = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="+", default=new_inventory)