import urllib, json, random
import re
from api.models import Recipe, Ingredient
from recipe_formatter import simplifyIngredients


def process_name(name):
    name_rep = name
    name_rep = name_rep.replace("tablespoons", "")
    name_rep = name_rep.replace("tablespoon", "")
    name_rep = re.sub('[0-9]', '', name_rep)
    name_rep = re.sub('cup[s]?', '', name_rep)
    return name_rep

recipes = []

with open('recipes.json') as json_data:
    d = json.load(json_data)

    for key in d.keys():
        recipe_data = d[key]
        ingredients = []
        for ingredient in recipe_data['ingredients']:
            m = re.search('(?P<name>[a-zA-Z 0-9]+) ADVERTISEMENT', ingredient)
            if(m):
                ingredients.append(m.group('name'))
        
        ingredients = simplifyIngredients(ingredients)
        ingredients = [list(x)[0] for x in ingredients]
        ingredient_objs = []
        for i in ingredients:
            ingredient_obj = Ingredient(name=i)
            ingredient_objs.append(ingredient_obj)
            #ingredient_obj.save()
            print ingredient_obj
                
        if('title' in recipe_data.keys() and 'instructions' in recipe_data.keys() and 'picture_link' in recipe_data.keys()):
            recipe = Recipe(name=recipe_data['title'], 
                     instructions=recipe_data['instructions'], 
                     source=recipe_data['picture_link'])
            print recipe
            #recipe.save()
            for i in ingredient_objs:
                 recipe.ingredients.add(i)
            recipes.append(recipe)
            
        if(len(recipes)==10):
            break
