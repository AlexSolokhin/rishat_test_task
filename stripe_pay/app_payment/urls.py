from django.urls import path
from app_payment.views import ItemsListView, PreBuyItemView, StripeSessionItemApiView,\
    OrdersListView, PreOrderView, StripeSessionOrderApiView, SuccessView

urlpatterns = [
    path('', ItemsListView.as_view(), name='items_list'),
    path('item/<int:pk>', PreBuyItemView.as_view(), name='pre_buy'),
    path('buy/<int:pk>', StripeSessionItemApiView.as_view(), name='stripe_session_item_api'),
    path('orders', OrdersListView.as_view(), name='orders_list'),
    path('order/<int:pk>', PreOrderView.as_view(), name='pre_order'),
    path('make_order/<int:pk>', StripeSessionOrderApiView.as_view(), name='stripe_session_order_api'),
    path('success', SuccessView.as_view(), name='success_page'),
]
