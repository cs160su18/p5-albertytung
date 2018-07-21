from django.shortcuts import render
from django.core import serializers
from .forms import RecipeForm, StepsForm, SearchForm



from life.models import * 
def index(request):
    return render(request, 'life/index.html')
  

  
def results(request):
    return render(request, 'life/results.html')
    

def search(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            # render the proper page
            
    context { 
      'recipes' : recipes
    }
    form = SearchForm()
    return render(request, 'life/search.html', {'form' : form})
  
def recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            curTitle = form.cleaned_data['title']
            curDescription = form.cleaned_data['description']
            # you should be able to extract inputs from the form here
            # store the data
            
            # check if existing
            existingRecipe = Recipe.objects.filter(name=curTitle)
            if not existingRecipe:
              newRecipe = Recipe(title=curTitle, description=curDescription)
              # if not existing, create an entry
              newRecipe.save()
        
    form = RecipeForm()
    return render(request, 'life/recipe.html', {'form' : form})
  
def steps(request):
    if request.method == 'POST':
        form = StepsForm(request.POST)
        if form.is_valid():
            curTitle = form.cleaned_data['title']
            curStepOne = form.cleaned_data['stepOne']
            curStepTwo = form.cleaned_data['stepTwo']
            curStepThree = form.cleaned_data['stepThree']
            
            existingRecipe = Recipe.objects.filter(name=curTitle)
            
            if existingRecipe:
              existingRecipeId = existingRecipe.id
              newSteps = Steps(stepOne=curStepOne, stepTwo=curStepTwo, stepThree=curStepThree, recipeKey=existingRecipeId)
            # if existing, do nothing
          
            # if not existing, create an entry
              newSteps.save()
            # you should be able to extract inputs from the form here
            # store the data
            # check to see if title exists
            # if does not exist, do nothing
            # otherwise, add it as a set of steps for the recipe (matching foreignkey)
       
    
    form = StepsForm()
    return render(request, 'life/steps.html', {'form' : form})
  
  