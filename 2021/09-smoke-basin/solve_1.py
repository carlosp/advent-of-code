#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
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

	return sum(1 + int(heightmap[x][y]) for x, y in basinSizes)


if __name__ == '__main__':
	heightmap = [list(line.strip()) for line in sys.stdin.readlines()]
	print(solve(heightmap))
