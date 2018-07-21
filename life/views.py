from django.shortcuts import render
from django.core import serializers
from .forms import RecipeForm, StepsForm, SearchForm



from life.models import * 
def index(request):
    return render(request, 'life/index.html')
  

  
def results(request):
    return render(request, 'life/results.html')
    

def search(request):
    curTitle = ""
    steps = ""
    
    print("going through search")
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print("entered search post request")
        if form.is_valid():
            print("form is valid")
            curTitle = form.cleaned_data['title']
            print("the title is: " + curTitle)
            # render the proper page
            
            curRecipe = None
    
            matchingRecipes = Recipe.objects.filter(title=curTitle)
            print("possibly matching recipes")
            if matchingRecipes:
              print("definitely matching recipes")
              curRecipe = matchingRecipes[0]
              curRecipeId = curRecipe.id
              
              steps = curRecipe.steps_set.all()
              print("The steps for the recipe are: " + str(steps))
              
    form = SearchForm()
    context =  { 
      'title' : curTitle,
      'form' : form,
      'steps' : steps
    }
    print("The context" + str(context))
    return render(request, 'life/search.html', context)
  
def recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            curTitle = form.cleaned_data['title']
            curDescription = form.cleaned_data['description']
            # you should be able to extract inputs from the form here
            # store the data
            
            # check if existing
            existingRecipe = Recipe.objects.filter(title=curTitle)
            if not existingRecipe:
              print("Creating a new recipe; title: " + curTitle + " curDescription: " + curDescription)
              
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
            
            existingRecipe = Recipe.objects.filter(title=curTitle)[0]
            
            if existingRecipe:
            
              existingRecipeId = existingRecipe.id
              print("Creating a new recipe" + curStepOne + " " + curStepTwo + " " + curStepThree)
              newSteps = Steps(stepOne=curStepOne, stepTwo=curStepTwo, stepThree=curStepThree, recipeKey=existingRecipe)
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
  
  