#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countFreshIngredientIds(freshIdRanges: list[list[int, int]]) -> int:
	sortedIdRanges = sorted(freshIdRanges)
	mergedIdRanges = [sortedIdRanges[0]]

	for currentRange in sortedIdRanges[1:]:
		lastRange = mergedIdRanges[-1]

		if currentRange[0] <= lastRange[1]:
			lastRange[1] = max(lastRange[1], currentRange[1])
		else:
			mergedIdRanges.append(currentRange)

	return sum(rangeEnd - rangeStart + 1 for rangeStart, rangeEnd in mergedIdRanges)


if __name__ == '__main__':
	freshIdRangesDefinitions, _ = sys.stdin.read().split('\n\n')
	freshIdRanges = [list(map(int, range.split('-'))) for range in freshIdRangesDefinitions.splitlines()]

	print(countFreshIngredientIds(freshIdRanges))
