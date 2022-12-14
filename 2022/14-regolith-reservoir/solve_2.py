#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys

SAND_SOURCE = (500, 0)

def getRockTiles(rockPaths):
	filledTiles = set()

	for rockPath in rockPaths:
		for (x1, y1), (x2, y2) in itertools.pairwise(rockPath):
			for x in range(min(x1, x2), max(x1, x2) + 1):
				for y in range(min(y1, y2), max(y1, y2) + 1):
					filledTiles.add((x, y))

	return filledTiles

def solve(rockPaths):
	filledTiles = getRockTiles(rockPaths)
	floorY = 2 + max(y for _, y in filledTiles)
	numRockTiles = len(filledTiles)

	while SAND_SOURCE not in filledTiles:
		nx, ny = SAND_SOURCE
		isSandMoving = True

		while isSandMoving and ny < floorY:
			x, y, ny = nx, ny, ny + 1
			isSandMoving = False

			for nx in (x, x - 1, x + 1):
				if (nx, ny) not in filledTiles:
					isSandMoving = True
					break

		filledTiles.add((x, y))

	return len(filledTiles) - numRockTiles


if __name__ == '__main__':
	rockPaths = [
		[tuple(map(int, point.split(','))) for point in line.split('->')]
		for line in sys.stdin.readlines()
	]

	print(solve(rockPaths))
