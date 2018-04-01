from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.forms.models import model_to_dict

from .models import Ingredient, Recipe


def _get_recipe_list(ingredients):
    result_list = []
    recipes = Recipe.objects.all()
    
    for r in recipes:
        matches = []
        not_matches = []
        points = 0
        i_list = []
        for i in r.ingredients.all():
            i_list.append(i.name)
        print i_list
        
        for i in i_list:
            if i.strip() in ingredients:
                matches.append(i.strip())
                points = points + 1
            else:
                not_matches.append(i.strip())
        if points > 0: 
            recipe  = dict()
            recipe['points'] = points + 0.5*r.rating
            recipe['matches'] = matches
            recipe['not_matches'] = not_matches
            recipe['info'] = model_to_dict(r)
            result_list.append(recipe)
    
    newlist = sorted(result_list, key=lambda k: k['points'], reverse=True) 
    return newlist
        
def index(request):
    response_data = {}
    response_data['result'] = ['Dim Sum', 'Laksa', 'Burger']
    response_data['message'] = 'Some error message'
    return JsonResponse(response_data)

def get_recipe_list(request):
    query_list = {}
    query_list['q'] = request.GET.get('i').split(',')

    # ingredients = QueryDict(query_list)['i']
    recipe_list = _get_recipe_list(query_list['q'])
    return JsonResponse({'results': recipe_list})

def increment_rating(request, id):
    recipe = Recipe.objects.get(id=int(id))
    recipe.rating = recipe.rating + 1
    recipe.save()
    return HttpResponse("Success")