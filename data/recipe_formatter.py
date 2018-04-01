#!/usr/bin/env python
#This project was copied from: https://flothesof.github.io/probabilistic-ingredients.html

# import pandas as pd
import codecs, re, itertools, json

json_data = open('train.json')
data = json.load(json_data)
#df_train = pd.read_json(codecs.open('train.json', 'r', 'utf-8'))

df_train = []
for d in data:
	df_train.append(d['ingredients'])


all_ingredients_text = []
for ingredient_list in df_train:
	all_ingredients_text += [ing.lower() for ing in ingredient_list]

splitter = re.compile('[,. ]+')
all_words = []
for ingredient in all_ingredients_text:
	all_words += re.split(splitter, ingredient)

def to_ingredient(text):
	"Transforms text into an ingredient."
	return frozenset(re.split(re.compile('[,. ]+'), text))

all_ingredients = [to_ingredient(text) for text in all_ingredients_text]


def candidates(ingredient):
	"Returns a list of candidate ingredients obtained from the original ingredient by keeping at least one of them."
	n = len(ingredient)
	possible = []
	for i in range(1, n + 1):
		possible += [frozenset(combi) for combi in itertools.combinations(ingredient, i)]
	return possible

from collections import Counter
#print(all_ingredients)
c = Counter(all_ingredients)

from collections import defaultdict
probability = defaultdict(lambda: 1, c.most_common())


def best_replacement(ingredient):
	"Computes best replacement ingredient for a given input."
	return max(candidates(ingredient), key=lambda c: probability[c])

def simplifyIngredients (ingredient_list):
	simplified_ingredient_list = [None for i in range (len(ingredient_list))]
	for i in range(len(ingredient_list)):
		simplified_ingredient_list[i] = best_replacement(to_ingredient(ingredient_list[i]))if (ingredient_list[i] != "ADVERTISEMENT") else None
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
	print ("\n")

if __name__ == "__main__":
	main()
