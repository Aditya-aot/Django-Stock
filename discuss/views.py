from django.shortcuts import render

# Create your views here.


def discuss(request) :
    a=['a','b','c','d','c']
    context = {'a':a}
    return render(request, 'discuss/discuss.html',context)
