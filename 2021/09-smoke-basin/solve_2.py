#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import math
import sys
from functools import cache

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solve(heightmap):
	@cache
	def getBasin(x, y):
		for nx, ny in [(x + dx, y + dy) for dx, dy in DIRECTIONS]:
			if 0 <= nx < len(heightmap) and 0 <= ny < len(heightmap[nx]) and heightmap[nx][ny] < heightmap[x][y]:
				return getBasin(nx, ny)

		return x, y


	basinSizes = collections.Counter([
		getBasin(x, y)
		for x in range(len(heightmap))
		for y in range(len(heightmap[x]))
		if heightmap[x][y] != '9'
	])

	return math.prod(entry[1] for entry in basinSizes.most_common(3))


if __name__ == '__main__':
	heightmap = [list(line.strip()) for line in sys.stdin.readlines()]
	print(solve(heightmap))
