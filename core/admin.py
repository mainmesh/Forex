from django.contrib import admin
from .models import Profile, Link
from .models import TradeLogin

class LinkInline(admin.TabularInline):
    model = Link
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [LinkInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(TradeLogin)