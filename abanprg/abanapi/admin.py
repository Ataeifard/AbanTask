from django.contrib import admin
from abanapi.models import Sell

class SellAdmin(admin.ModelAdmin):
    list_display = ("user", "crypto_name", "crypto_amount", "timestamp",)
    search_fields = ("user", "crypto_name",)
    list_filter = ("user", "crypto_name",)

admin.site.register(Sell, SellAdmin)