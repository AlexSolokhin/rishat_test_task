import stripe
from django.core.management.base import BaseCommand
from stripe_pay.settings import STRIPE_SK
from app_payment.models import Tax


class Command(BaseCommand):
    help = 'Создание дефолтного налога при запуске проекта с новой учётной записью stripe'

    def handle(self, *args, **kwargs):
        stripe.api_key = STRIPE_SK

        sales_tax = stripe.TaxRate.create(display_name="Sales Tax", inclusive=False, percentage=7)

        new_tax = Tax.objects.create(stripe_tax_id=sales_tax.id,
                                     tax_name='Sales Tax', inclusive=False, percentage=7)
        new_tax.save()
