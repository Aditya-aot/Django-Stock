from django.shortcuts import render


from .forms import search_day ,Form
# Create your views here.

# from .forms import search_day
# Create your views here.


def chat(request, pk ) :

    context = { 'pk':pk,

    }
    return render(request, 'discuss/chat.html',context)

