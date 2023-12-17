from django.contrib import admin
from eggtart.models import Eggtart

@admin.register(Eggtart)
class EggtartAdmin(admin.ModelAdmin):
    list_display = ["shop", "thumbnail"]



