#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys

Point = tuple[int, int]
BoundingBox = tuple[Point, Point]

def collides(edges: list[BoundingBox], rectangle: BoundingBox) -> bool:
	(rectMinX, rectMinY), (rectMaxX, rectMaxY) = rectangle

	for (edgeMinX, edgeMinY), (edgeMaxX, edgeMaxY) in edges:
		if rectMinX < edgeMaxX and rectMinY < edgeMaxY and rectMaxX > edgeMinX and rectMaxY > edgeMinY:
			return True

	return False

def getEdgesAsBoundingBoxes(points: list[Point]) -> list[BoundingBox]:
	return [
		((min(x1, x2), min(y1, y2)), ((max(x1, x2), max(y1, y2))))
		for (x1, y1), (x2, y2) in itertools.pairwise(points + [points[0]])
	]

def solve(redTiles: list[Point]) -> int:
	edges, maxArea = getEdgesAsBoundingBoxes(redTiles), 0

	for (x1, y1), (x2, y2) in itertools.combinations(redTiles, 2):
		minX, minY, maxX, maxY = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

		if (area := (maxX - minX + 1) * (maxY - minY + 1)) > maxArea and not collides(edges, ((minX, minY), (maxX, maxY))):
			maxArea = area

	return maxArea


if __name__ == '__main__':
	redTiles = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(solve(redTiles))
