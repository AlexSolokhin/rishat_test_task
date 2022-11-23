from django.contrib import admin
from app_payment.models import Item, Order, OrderItem, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Item в админке
    """

    list_display = ('name', 'price', 'short_description')
    list_display_links = ('name',)
    ordering = ('price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Order в админке
    """

    list_display = ('id', 'created')
    list_display_links = ('id',)
    ordering = ('created',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели OrderItem в админке
    """

    list_display = ('item', 'order', 'quantity')
    list_display_links = ('item',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Discount в админке
    """

    list_display = ('percent_off', 'amount_off')
    list_display_links = ('percent_off', 'amount_off')
    ordering = ('percent_off', 'amount_off')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Tax в админке
    """

    list_display = ('tax_name', 'percentage', 'inclusive')
    list_display_links = ('tax_name',)
    ordering = ('percentage',)
