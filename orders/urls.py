from django.urls import path

from orders.views import (CanceledTemplateView, CreateOrderView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = "orders"

urlpatterns = [
    path("order-create/", CreateOrderView.as_view(), name="order_create"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order-canceled/", CanceledTemplateView.as_view(), name="order_canceled"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("", OrderListView.as_view(), name="orders_list"),
]
