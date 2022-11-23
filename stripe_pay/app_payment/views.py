from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import JsonResponse
from stripe_pay.settings import STRIPE_PK
from app_payment.models import Item, Order, OrderItem
from app_payment.utils.stripe_session import create_stripe_item_session, create_stripe_order_session


class ItemsListView(ListView):
    """
    Отображение всех продуктов
    """

    model = Item
    template_name = 'app_payments/items_list.html'
    context_object_name = 'items'


class PreBuyItemView(DetailView):
    """
    Отображение одного продукта с кнопкой 'Buy'
    """

    model = Item
    template_name = 'app_payments/pre_buy.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(PreBuyItemView, self).get_context_data(**kwargs)
        context['stripe_pk'] = STRIPE_PK
        return context


class StripeSessionItemApiView(View):
    """
    APi создаёт Stripe сессию для оплаты продукта
    """

    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        session = create_stripe_item_session(item)

        return JsonResponse(session, json_dumps_params={'indent': 2})


class SuccessView(View):
    """
    Страница успешной оплаты
    """

    def get(self, request):
        return render(request, 'app_payments/success.html')


class OrdersListView(ListView):
    """
    Отображение всех заказов
    """

    model = Order
    template_name = 'app_payments/orders_list.html'
    context_object_name = 'orders'


class PreOrderView(DetailView):
    """
    Отображение одного заказа с кнопкой Order
    """

    model = Order
    template_name = 'app_payments/pre_order.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super(PreOrderView, self).get_context_data(**kwargs)
        context['stripe_pk'] = STRIPE_PK
        return context


class StripeSessionOrderApiView(View):
    """
    APi создаёт Stripe сессию оплаты заказа
    """

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        session = create_stripe_order_session(order)

        return JsonResponse(session, json_dumps_params={'indent': 2})
