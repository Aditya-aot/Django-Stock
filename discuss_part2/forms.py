from django import forms
from django.forms import ModelForm
from .models import TutorialCategory
# from django.form import ModelForm



days_s= [(10,10),(50,50),(100,100),(500,500)]
class search_day(forms.Form) :
    stock = forms.ChoiceField(choices=days_s)


class Form(ModelForm):
    class Meta:
        # category =  forms.ChoiceField( choices=['1','2','3'], required=False)
        model = TutorialCategory
        fields = [
            'tutorial_category' ,
            
        ]