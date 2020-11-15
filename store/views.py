from django.shortcuts import render

# Create your views here.
def storeView(request):
    context = {}
    return render(request,'store/store.html',context)

def checkoutView(request):
    context = {}
    return render(request,'store/checkout.html',context)

def cartView(request):
    context = {}
    return render(request,'store/cart.html',context)
