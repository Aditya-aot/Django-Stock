from django.shortcuts import render


from .forms import search_day ,Form
# Create your views here.

# from .forms import search_day
# Create your views here.


def discuss(request) :

    form = search_day()
    form2 = Form()
    a=['a','b','c','d','c']
    if request.method =='POST' :
        form = search_day(request.POST, request.FILES)
        if form.is_valid() :
            stock = form.cleaned_data['stock']

        context = {'a':a ,
                    'form':form ,
                    'stock' : stock ,
                        }
        return render(request, 'discuss/discuss.html',context)
        
    context = {'a':a ,
                    'form':form ,
                    'form2':form2
                        }
    return render(request, 'discuss/discuss.html',context) 


def chat(request, pk ) :

    context = { 'pk':pk,

    }
    return render(request, 'discuss/chat.html',context)

