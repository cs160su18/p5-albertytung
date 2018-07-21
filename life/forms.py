from django import forms
from django.utils.html import mark_safe
class RecipeForm(forms.Form):
    # process recipe, make different titles
    
    title = forms.CharField(label='title', max_length=50)
    description = forms.CharField(label='description', max_length=100)
    
class SearchForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    
class StepsForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    stepOne = forms.CharField(label='stepOne', max_length=100)
    stepTwo = forms.CharField(label='stepTwo', max_length=100)
    stepThree = forms.CharField(label='stepThree', max_length=100)
    