from django.urls import path
from core import views

urlpatterns = [
    path('', views.orders_view, name='home'),
    path('orders/', views.orders_view, name='orders'),
    path('orders/<int:order_id>/take/', views.order_take, name='order_take'),
    path('orders/<int:order_id>/done/', views.order_done, name='order_done'),
    path('orders/<int:order_id>/refuse/', views.order_refuse, name='order_refuse'),
]
