from django.contrib import admin
from main_app.models import SubscriptionTier, Subscription, Users, UserPackStatus, UserCardStatus, CardPack, FlashCard


# Register your models here.
@admin.register(SubscriptionTier)
class SubscriptionTierAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
