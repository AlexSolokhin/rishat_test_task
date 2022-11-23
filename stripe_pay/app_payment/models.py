from django.db import models


class Item(models.Model):
    """
    Модель, описывающая продукт.
    """

    name = models.CharField(verbose_name='item name', max_length=50)
    description = models.TextField(verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')

    @property
    def short_description(self):
        return self.description[:20]

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('price',)

    def __str__(self):
        return self.name


class Discount(models.Model):
    """
    Модель, описывающая скидку.
    """

    stripe_coupon_id = models.CharField(verbose_name='stripe coupon id', max_length=250)
    percent_off = models.IntegerField(verbose_name='discount in percents')
    amount_off = models.IntegerField(verbose_name='discount in amount')

    class Meta:
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'

    def __str__(self):
        return f'Percent off: {self.percent_off}; amount off: {self.amount_off}'


class Tax(models.Model):
    """
    Модель, описывающая схему налогообложения.
    """

    stripe_tax_id = models.CharField(verbose_name='stripe tax id', max_length=250)
    tax_name = models.CharField(verbose_name='tax name', max_length=50)
    percentage = models.FloatField(verbose_name='tax percentage')
    inclusive = models.BooleanField(verbose_name='is inclusive')

    class Meta:
        verbose_name = 'tax'
        verbose_name_plural = 'taxes'

    def __str__(self):
        return self.tax_name


class Order(models.Model):
    """
    Модель, описывающая заказ.
    """

    created = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, verbose_name='discount',
                                 related_name='orders', blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, verbose_name='tax',
                            related_name='taxes', blank=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ('created',)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    """
    Модель, описывающая одну позицию в заказе.
    Необходима для уточнения количества единиц продукта в заказе.
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item', related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='order', related_name='items')
    quantity = models.PositiveIntegerField(verbose_name='quantity')

    class Meta:
        verbose_name = 'position'
        verbose_name_plural = 'positions'

    def __str__(self):
        return f'Order {self.order.id}: position {self.item.id} - {self.quantity}'
