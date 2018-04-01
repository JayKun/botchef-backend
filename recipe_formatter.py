#!/usr/bin/env python
#This project was copied from: https://flothesof.github.io/probabilistic-ingredients.html

import pandas as pd

import codecs
df_train = pd.read_json(codecs.open('train.json', 'r', 'utf-8'))

#df_train.head()
#print (df_train.head())

all_ingredients_text = []
for ingredient_list in df_train.ingredients:
	all_ingredients_text += [ing.lower() for ing in ingredient_list]

#len(all_ingredients_text)
#print(len(all_ingredients_text))

#len(set(all_ingredients_text))
#print(len(set(all_ingredients_text)))

import re
#re.split(re.compile('[,. ]+'), 'KRAFT Shredded Pepper Jack Cheese with a TOUCH OF PHILADELPHIA')

splitter = re.compile('[,. ]+')
all_words = []
for ingredient in all_ingredients_text:
	all_words += re.split(splitter, ingredient)

#len(all_words)
#print(len(all_words))

#len(set(all_words))
#print(len(set(all_words)))

#sorted(set(all_ingredients_text), key=len, reverse=True)[:50]
#print(sorted(set(all_ingredients_text), key=len, reverse=True)[:50])


def to_ingredient(text):
	"Transforms text into an ingredient."
	return frozenset(re.split(re.compile('[,. ]+'), text))

all_ingredients = [to_ingredient(text) for text in all_ingredients_text]

#all_ingredients[:10]
#print(all_ingredients[:10])

import itertools

def candidates(ingredient):
	"Returns a list of candidate ingredients obtained from the original ingredient by keeping at least one of them."
	n = len(ingredient)
	possible = []
	for i in range(1, n + 1):
		possible += [frozenset(combi) for combi in itertools.combinations(ingredient, i)]
	return possible

#candidates(to_ingredient("tomato and herb pasta sauce"))
#print(candidates(to_ingredient("tomato and herb pasta sauce")))

#candidates(to_ingredient('knorr chicken flavor bouillon cube'))
#print(candidates(to_ingredient('knorr chicken flavor bouillon cube')))

from collections import Counter

c = Counter(all_ingredients)

#c.most_common(20)
#print(c.most_common(20))

from collections import defaultdict
probability = defaultdict(lambda: 1, c.most_common())

#probability[to_ingredient('pasta and herb')]
#print(probability[to_ingredient('pasta and herb')])

#probability[to_ingredient('tomato sauce')]
#print(probability[to_ingredient('tomato sauce')])

def best_replacement(ingredient):
	"Computes best replacement ingredient for a given input."
	return max(candidates(ingredient), key=lambda c: probability[c])



'''
#best_replacement(to_ingredient("tomato sauce"))
print(best_replacement(to_ingredient("tomato sauce")))

#best_replacement(to_ingredient("pasta and herb"))
print(best_replacement(to_ingredient("pasta and herb")))

#best_replacement(to_ingredient("kraft mexican style shredded four cheese with a touch of philadelphia"))
print(best_replacement(to_ingredient("kraft mexican style shredded four cheese with a touch of philadelphia")))


pd.DataFrame([(text, 
				" ".join(best_replacement(to_ingredient(text)))) for text in sorted(set(all_ingredients_text), key=len, reverse=True)[:50]],
				columns=['original ingredient', 'improved ingredient'])
'''

def simplifyIngredients (ingredient_list):
	simplified_ingredient_list = [None for i in range (len(ingredient_list))]
	for i in range(len(ingredient_list)):
		simplified_ingredient_list[i] = best_replacement(to_ingredient(ingredient_list[i])) if (ingredient_list[i] != "ADVERTISEMENT") else None
	return simplified_ingredient_list

def main ():
	wordy_ingredients = [
		"1/2 cup packed brown sugar ADVERTISEMENT",
		"1/2 cup ketchup ADVERTISEMENT",
		"1 1/2 pounds lean ground beef ADVERTISEMENT",
		"3/4 cup milk ADVERTISEMENT",
		"2 eggs ADVERTISEMENT",
		"1 1/2 teaspoons salt ADVERTISEMENT",
		"1/4 teaspoon ground black pepper ADVERTISEMENT",
		"1 small onion, chopped ADVERTISEMENT",
		"1/4 teaspoon ground ginger ADVERTISEMENT",
		"3/4 cup finely crushed saltine cracker crumbs ADVERTISEMENT",
		"ADVERTISEMENT"
	]
	
	simple_ingredients = simplifyIngredients(wordy_ingredients)
	
	print ("****SIMPLIFIED INGREDIENTS****")
	for i in range(len(wordy_ingredients)):
		print ("\tWordy: {0}\tSimple: {1}\tScore: {2}".format(wordy_ingredients[i], simple_ingredients[i], str(probability[simple_ingredients[i]])))
		#print ("\tWordy: " + str(wordy_ingredients[i]) + "\tSimple: " + str(simple_ingredients[i]) + "Score: " + str(probability[simple_ingredients[i]]))
	print ("\n")
	#print(str(simple_ingredients))
	

	'''
	print ("Converting recipes_raw/recipes_raw_nosource_ar.json to list of strings of simplified ingredients")
	df_simplify = pd.read_json(codecs.open('recipes_raw/recipes_raw_nosource_ar.json', 'r', 'utf-8'))
	
	single_recipe = df_simplify[0]
	single_ingredient_list = (single_recipe.ingredients)[0]
	print (str(single_ingredient_list))
	'''
	
	'''
	for ingredient_list in df_train.ingredients:
		all_ingredients_text += [ing.lower() for ing in ingredient_list]
	'''

if __name__ == "__main__":
	main()
