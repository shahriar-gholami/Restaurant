from django.contrib import admin
from .models import Category, Item, OrderItem, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'count']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['shamsi_created_date', 'status']

    def shamsi_created_date(self, obj):
        return obj.shamsi_created_date

    shamsi_created_date.short_description = 'Created Date (Shamsi)'
