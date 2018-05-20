from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class ItemType(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Inventory(models.Model):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="+", default=Inventory.objects.create)
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
    #location = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="items")
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.quantity) + " " + str(self.itemtype)

class Factory(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #storage = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="+", default=Inventory.objects.create)
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class TradeRequest(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="outgoing_requests")
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="incoming_requests")
    accepted = models.BooleanField(default=False)
    #requested_items = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="+", default=Inventory.objects.create)
    #offered_items = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="+", default=Inventory.objects.create)