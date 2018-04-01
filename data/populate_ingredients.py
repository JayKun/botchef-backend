import urllib, json, random
import re
from api.models import Ingredient

json_data = open('recipes.json')
d = json.load(json_data)
ingredients = []
for key in d.keys():
    recipe = d[key]
    if('ingredients' in recipe.keys()):
        for ingredient in recipe['ingredients']:
            m = re.search('(?P<name>[a-zA-Z 0-9]+) ADVERTISEMENT', ingredient)
            if(m):
                print m.group('name')
                name_rep = m.group('name')
                name_rep = name_rep.replace("tablespoons", "")
                name_rep = name_rep.replace("tablespoon", "")
                name_rep = re.sub('[0-9]', '', name_rep)
                name_rep = re.sub('cup[s]?', '', name_rep)
                ingredient_obj = Ingredient(name=name_rep)
                ingredients.append(ingredient_obj)
        if(len(ingredients)>50):
            break
Ingredient.objects.bulk_create(ingredients)