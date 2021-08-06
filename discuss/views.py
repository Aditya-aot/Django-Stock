from django.shortcuts import render

from .forms import search_day
# Create your views here.


def discuss(request) :

    form = search_day()

    a=['a','b','c','d','c']
    context = {'a':a ,
                'form':form ,
                    }
    return render(request, 'discuss/discuss.html',context)
