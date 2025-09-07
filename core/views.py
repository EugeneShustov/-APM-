from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from core.models import Order

def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

@require_POST
def order_take(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.take_to_work()
    return redirect('orders')

@require_POST
def order_done(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.mark_done()
    return redirect('orders')

@require_POST
def order_refuse(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.mark_refused()
    return redirect('orders')

