#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
import sys
from functools import cache

def countPathsVisiting(graph: dict[str, list[str]], nodesToVisit: list[str]) -> int:
	@cache
	def countPathsBetween(startNode: str, endNode: str) -> int:
		return 1 if startNode == endNode else sum(countPathsBetween(nextNode, endNode) for nextNode in graph.get(startNode, []))


	return math.prod(countPathsBetween(startNode, endNode) for startNode, endNode in itertools.pairwise(nodesToVisit))


if __name__ == '__main__':
	deviceOutputs = { device[:-1]: outputs for device, *outputs in map(str.split, sys.stdin.readlines()) }

	print(countPathsVisiting(deviceOutputs, ['you', 'out']))
