#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

def step(pairCounts, elementCounts, rules):
	newPairs = collections.Counter()

	for (element1, element2), count in pairCounts.items():
		newElement = rules[element1 + element2]
		newPairs[element1 + newElement] += count
		newPairs[newElement + element2] += count
		elementCounts[newElement] += count

	return newPairs

def solve(polymerTemplate, insertionRules):
	elementCounts = collections.Counter(polymerTemplate)
	pairCounts = collections.Counter(map(''.join, zip(polymerTemplate, polymerTemplate[1:])))

	for _ in range(10):
		pairCounts = step(pairCounts, elementCounts, insertionRules)

	return elementCounts.most_common()[0][1] - elementCounts.most_common()[-1][1]


if __name__ == '__main__':
	polymerTemplate, ruleLines = sys.stdin.read().split('\n' * 2)
	insertionRules = dict(line.split(' -> ') for line in ruleLines.splitlines())

	print(solve(polymerTemplate, insertionRules))
