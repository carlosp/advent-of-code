#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

DIRECTIONS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def surfaceArea(cubeList):
	cubeSet = set(cubeList)
	return sum(
		(x + dx, y + dy, z + dz) not in cubeSet
		for x, y, z in cubeList
		for dx, dy, dz in DIRECTIONS
	)


if __name__ == '__main__':
	cubeList = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(surfaceArea(cubeList))
