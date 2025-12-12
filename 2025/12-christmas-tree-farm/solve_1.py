#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countRegionsThatCanFitPresents(presentShapes: dict[int, list[str]], regions: list[tuple[int, int, list[int]]]):
	minShapeSizes = { shapeIdx: sum(row.count('#') for row in shape) for shapeIdx, shape in presentShapes.items() }

	return sum(
		sum(minShapeSizes[shapeIdx] * quantity for shapeIdx, quantity in enumerate(shapeQuantities)) <= width * length
		for width, length, shapeQuantities in regions
	)


if __name__ == '__main__':
	*presentShapesDefinitions, regionsDefinitions = sys.stdin.read().split('\n\n')
	presentShapes = { int(shapeIdx[:-1]): shape for shapeIdx, *shape in map(str.splitlines, presentShapesDefinitions) }
	regions = [
		tuple([*map(int, size[:-1].split('x')), list(map(int, shapeIds))])
		for size, *shapeIds in map(str.split, regionsDefinitions.splitlines())
	]

	print(countRegionsThatCanFitPresents(presentShapes, regions))
