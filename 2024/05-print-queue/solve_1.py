#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys
from functools import cmp_to_key

def solve(orderingRules: list[tuple[int, int]], updates: list[list[int]]) -> int:
	pagesAfter = collections.defaultdict(set)
	compareFn = lambda x, y: -1 if y in pagesAfter[x] else 1 if x in pagesAfter[y] else 0
	result = 0

	for x, y in orderingRules:
		pagesAfter[x].add(y)

	for update in updates:
		if update == (sortedUpdate := sorted(update, key=cmp_to_key(compareFn))):
			result += sortedUpdate[len(sortedUpdate) // 2]

	return result


if __name__ == '__main__':
	orderingRulesDefinitions, updatesDefinitions = sys.stdin.read().split('\n\n')
	orderingRules = [tuple(map(int, ruleDefinition.split('|'))) for ruleDefinition in orderingRulesDefinitions.splitlines()]
	updates = [list(map(int, updateDefinition.split(','))) for updateDefinition in updatesDefinitions.splitlines()]

	print(solve(orderingRules, updates))
