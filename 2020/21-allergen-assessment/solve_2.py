#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter
import sys

def parseFoods(rawFoods):
	foods = []

	for rawFood in rawFoods:
		ingredients, allergens = rawFood.strip().split(' (contains')
		ingredients = set(map(str.strip, ingredients.split(' ')))
		allergens = set(map(str.strip, allergens[:-1].split(',')))

		foods += [(ingredients, allergens)]

	return foods

def matchAllergensAndIngredients(foods):
	numAllergens = len(set.union(*(allergens for _, allergens in foods)))
	ingredientToAllergenMap = {}

	while len(ingredientToAllergenMap) < numAllergens:
		for ingredients, allergens in foods:
			for allergen in allergens - set(ingredientToAllergenMap.values()):
				candidateIngredients = set(ingredients) - set(ingredientToAllergenMap.keys())

				for otherIngredients, otherAllergens in foods:
					if allergen in otherAllergens:
						candidateIngredients &= otherIngredients

				if len(candidateIngredients) == 1:
					ingredientToAllergenMap[candidateIngredients.pop()] = allergen

	return ingredientToAllergenMap

def solve(rawFoods):
	foods = parseFoods(rawFoods)
	ingredientToAllergenMap = matchAllergensAndIngredients(foods)

	return ','.join(ingredient for ingredient, _ in sorted(ingredientToAllergenMap.items(), key=itemgetter(1)))


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
