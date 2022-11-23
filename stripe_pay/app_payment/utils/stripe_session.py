import stripe
from app_payment.models import Item, Order
from stripe_pay.settings import STRIPE_SK

stripe.api_key = STRIPE_SK


def create_stripe_item_session(item: Item) -> stripe.checkout.Session:
    """
    Создание сессии Stripe для одного продукта

    :param item: продукт, который предстоит оплатить
    :type item: Item
    :return: Сессия Stripe
    :rtype: stripe.checkout.Session
    """

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url=f'http://localhost:8000/item/{item.id}',
    )
    return session


def create_stripe_order_session(order: Order) -> stripe.checkout.Session:
    """
    Создание сессии Stripe для заказа

    :param order: заказ, который предстоит оплатить
    :type order: Order
    :return: Сессия Stripe
    :rtype: stripe.checkout.Session
    """

    if order.discount:
        discounts = [{'coupon': order.discount.stripe_coupon_id}]
    else:
        discounts = []

    if order.tax:
        tax_rate = [order.tax.stripe_tax_id]
    else:
        tax_rate = []

    line_items = []
    for item in order.items.all():
        line_item = {
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.item.name,
                },
                'unit_amount': item.item.price * 100,
            },
            'quantity': item.quantity,
            'tax_rates': tax_rate,
        }
        line_items.append(line_item)

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/',
        discounts=discounts
    )
    return session
