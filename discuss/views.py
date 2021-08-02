from django.shortcuts import render

# Create your views here.


def home(request) :
    context = {}
    return render(request, 'stock/base2.html',context)
