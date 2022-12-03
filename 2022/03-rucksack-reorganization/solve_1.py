#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import sys

ITEM_PRIORITIES = { letter: idx + 1 for idx, letter in enumerate(string.ascii_letters) }

def solve(rucksacks):
	result = 0

	for rucksack in rucksacks:
		mid = len(rucksack) // 2
		(repeatedItem,) = set(rucksack[:mid]) & set(rucksack[mid:])
		result += ITEM_PRIORITIES[repeatedItem]

	return result


if __name__ == '__main__':
	rucksacks = map(str.strip, sys.stdin.readlines())

	print(solve(rucksacks))
