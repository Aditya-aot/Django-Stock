from django import forms

# from django.form import ModelForm



days_s= [(10,10),(50,50),(100,100),(500,500)]
class search_day(forms.Form) :
    stock = forms.ChoiceField(choices=days_s)



