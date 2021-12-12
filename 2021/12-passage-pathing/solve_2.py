#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

CAVE_START = 'start'
CAVE_END = 'end'

def countPaths(graph, cave, visitedCaves, canVisitSmallCaveTwice):
	if cave == CAVE_END:
		return 1

	result = 0
	isSmallCave = cave[0].islower()
	isRepeatedVisit = cave in visitedCaves

	if isSmallCave:
		visitedCaves.add(cave)

	for next in graph[cave]:
		if next != CAVE_START and (next not in visitedCaves or canVisitSmallCaveTwice):
			result += countPaths(graph, next, visitedCaves, canVisitSmallCaveTwice and next not in visitedCaves)

	if isSmallCave and not isRepeatedVisit:
		visitedCaves.remove(cave)

	return result

def solve(edges):
	graph = collections.defaultdict(list)

	for cave1, cave2 in edges:
		graph[cave1].append(cave2)
		graph[cave2].append(cave1)

	return countPaths(graph, CAVE_START, set(), True)


if __name__ == '__main__':
	edges = [line.strip().split('-') for line in sys.stdin.readlines()]
	print(solve(edges))
