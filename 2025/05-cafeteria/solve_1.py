#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countFreshIngredientIds(freshIdRanges: list[tuple[int, int]], availableIds: list[int]) -> int:
	return sum(
		any(rangeStart <= id <= rangeEnd for rangeStart, rangeEnd in freshIdRanges)
		for id in availableIds
	)


if __name__ == '__main__':
	freshIdRangesDefinitions, availableIdsDefinitions = sys.stdin.read().split('\n\n')
	freshIdRanges = [tuple(map(int, range.split('-'))) for range in freshIdRangesDefinitions.splitlines()]
	availableIds = list(map(int, availableIdsDefinitions.splitlines()))

	print(countFreshIngredientIds(freshIdRanges, availableIds))
