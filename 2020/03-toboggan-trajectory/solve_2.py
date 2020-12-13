#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def countTrees(areaMap, slope):
	numTrees = 0
	row, col = 0, 0
	height, width = len(areaMap), len(areaMap[0])

	while row < height:
		numTrees += areaMap[row][col % width] == '#'
		col += slope[0]
		row += slope[1]

	return numTrees


if __name__ == '__main__':
	areaMap = list(map(str.strip, sys.stdin.readlines()))
	print(math.prod([countTrees(areaMap, slope) for slope in SLOPES]))
