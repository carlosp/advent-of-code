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

def exteriorSurfaceArea(cubeList):
	def floodFill(startPosition):
		airCubes, isAirPocket = [], True
		q = [startPosition]

		while q:
			x, y, z = q.pop()

			if minX <= x <= maxX and minY <= y <= maxY and minZ <= z <= maxZ:
				if (x, y, z) not in visited:
					visited.add((x, y, z))
					airCubes += [(x, y, z)]
					q.extend((x + dx, y + dy, z + dz) for dx, dy, dz in DIRECTIONS)
			else:
				isAirPocket = False

		return airCubes, isAirPocket

	minX = min(x for x, _, _ in cubeList)
	maxX = max(x for x, _, _ in cubeList)
	minY = min(y for _, y, _ in cubeList)
	maxY = max(y for _, y, _ in cubeList)
	minZ = min(z for _, _, z in cubeList)
	maxZ = max(z for _, _, z in cubeList)
	airPocketsCubeList = []
	visited = set(cubeList)

	for x in range(minX + 1, maxX):
		for y in range(minY + 1, maxY):
			for z in range(minZ + 1, maxZ):
				if (x, y, z) not in visited:
					airCubeList, isAirPocket = floodFill((x, y, z))

					if isAirPocket:
						airPocketsCubeList += airCubeList

	return surfaceArea(cubeList) - surfaceArea(airPocketsCubeList)


if __name__ == '__main__':
	cubeList = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(exteriorSurfaceArea(cubeList))
