from django.contrib import admin

from .models import Contact, ReachOut


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ReachOut)
class RechOutAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "read",
    )
