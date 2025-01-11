from django.shortcuts import redirect, render
from .forms import *
import stripe
from .models import *
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def Products_page(request):
    product = Product.objects.all()
    context = {'product':product}

    return render(request,'product.html',context)


def DetailPage(request,name,id):
    product = Product.objects.get(id = id,name = name)
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'{product.name}',
                    },
                    'unit_amount': product.price*100, 
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return redirect(session.url, code=303)
    return render(request,'detail.html',{'product':product})

def payment_page(request,name,id):
    product = Product.objects.get(name = name,id = id)
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'{product.name}',
                    },
                    'unit_amount': 2000, 
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return redirect(session.url, code=303)
    return render(request, 'payment.html')


def payment_success(request):
    return render(request, 'success.html')

def payment_cancel(request):
    return render(request, 'cancel.html')
