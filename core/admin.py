from django.contrib import admin
from .models import Profile, Link

class LinkInline(admin.TabularInline):
    model = Link
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [LinkInline]

admin.site.register(Profile, ProfileAdmin)
