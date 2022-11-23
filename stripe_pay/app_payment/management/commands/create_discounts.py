import stripe
from django.core.management.base import BaseCommand
from stripe_pay.settings import STRIPE_SK
from app_payment.models import Discount


class Command(BaseCommand):
    help = 'Создание дефолтной скидки при запуске проекта с новой учётной записью stripe'

    def handle(self, *args, **kwargs):
        stripe.api_key = STRIPE_SK

        percent_coupon = stripe.Coupon.create(percent_off=20)

        percent_discount = Discount.objects.create(stripe_coupon_id=percent_coupon.id, percent_off=20, amount_off=0)
        percent_discount.save()
