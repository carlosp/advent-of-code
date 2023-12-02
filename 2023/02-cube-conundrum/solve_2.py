#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import math
import sys

def getMinCubesPresent(gameInfo):
	_, subsetsOfCubesList = gameInfo.split(':')
	minCubesPresent = collections.defaultdict(int)

	for subsetsOfCubes in subsetsOfCubesList.split(';'):
		for subsetOfCubes in subsetsOfCubes.split(','):
			numCubes, color = subsetOfCubes.strip().split(' ')
			minCubesPresent[color] = max(minCubesPresent[color], int(numCubes))

	return minCubesPresent.values()


if __name__ == '__main__':
	print(sum(
		math.prod(getMinCubesPresent(game))
		for game in sys.stdin.readlines()
	))
