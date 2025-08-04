from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item
from django.conf import settings
import stripe
# Create your views here.

stripe.api_key = settings.API_SECRET_KEY

def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/buy/success/'),
        cancel_url=request.build_absolute_uri('/buy/cancel/'),
    )
    return JsonResponse({'session_id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
        'stripe_public_key': settings.API_PUBLIC_KEY,
    }
    return render(request, 'item_detail.html', context)

def payment_success(request):
    return render(request, 'success.html')