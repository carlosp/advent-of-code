#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from functools import cache

def countAllWaysToMakeAnyDesign(availablePatterns: list[str], desiredDesigns: list[str]) -> int:
	@cache
	def countWaysToMakeDesign(design: str) -> int:
		return design == '' or sum(
			countWaysToMakeDesign(design.removeprefix(pattern))
			for pattern in availablePatterns
			if design.startswith(pattern)
		)

	return sum(map(countWaysToMakeDesign, desiredDesigns))


if __name__ == '__main__':
	availablePatternsDefinition, desiredDesignsDefinition = sys.stdin.read().split('\n\n')
	availablePatterns = availablePatternsDefinition.split(', ')
	desiredDesigns = desiredDesignsDefinition.splitlines()

	print(countAllWaysToMakeAnyDesign(availablePatterns, desiredDesigns))
