from django.shortcuts import render

# Create your views here.


def discuss(request) :
    context = {}
    return render(request, 'discuss/discuss.html',context)
