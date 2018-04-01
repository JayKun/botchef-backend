import urllib, json, random
import re
from api.models import Recipe, Ingredient

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
        # for ingredient in recipe_data['ingredients']:
        #     m = re.search('(?P<name>[a-zA-Z 0-9]+) ADVERTISEMENT', ingredient)
        #     if(m):
        #         ingredient_obj = Ingredient(name=process_name(m.group('name')))
        #         ingredients.append(ingredient_obj)
        #         ingredient_obj.save()
                
        if('title' in recipe_data.keys() and 'instructions' in recipe_data.keys() and 'picture_link' in recipe_data.keys()):
            recipe = Recipe(name=recipe_data['title'], 
                     instructions=recipe_data['instructions'], 
                     source=recipe_data['picture_link'])
            recipe.save()
            # for i in ingredients:
            #      recipe.ingredients.add(i)
            recipes.append(recipe)
            
        if(len(recipes)==30):
            break
