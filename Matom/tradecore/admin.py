from django.contrib import admin

from .models import ItemType, ItemStack, Profile, Factory

admin.site.register(ItemStack)
admin.site.register(ItemType)
admin.site.register(Factory)
admin.site.register(Profile)