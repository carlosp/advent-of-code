#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from functools import cache

def countPossibleDesigns(availablePatterns: list[str], desiredDesigns: list[str]) -> int:
	@cache
	def isDesignPossible(design: str) -> bool:
		return design == '' or any(
			isDesignPossible(design.removeprefix(pattern))
			for pattern in availablePatterns
			if design.startswith(pattern)
		)

	return sum(map(isDesignPossible, desiredDesigns))


if __name__ == '__main__':
	availablePatternsDefinition, desiredDesignsDefinition = sys.stdin.read().split('\n\n')
	availablePatterns = availablePatternsDefinition.split(', ')
	desiredDesigns = desiredDesignsDefinition.splitlines()

	print(countPossibleDesigns(availablePatterns, desiredDesigns))
