from django.shortcuts import render

# Create your views here.
def storeView(request):
    return render(request,template_name,context)

def productView(request):
    return render(request,template_name,context)

def catView(request):
    return render(request,template_name,context)
