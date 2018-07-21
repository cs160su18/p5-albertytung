from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
  path('index', views.index, name='index'),
    # path('activity/',views.activity, name='activity'),
   path('results', views.results, name='results'),
   path('search', views.search, name='search'),
  path('recipe', views.recipe, name='recipe'),
  path('steps', views.steps, name='steps'),

]