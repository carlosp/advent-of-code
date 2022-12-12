#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def parseMap(heightmap):
	heights = list(map(list, heightmap))
	startPositions = []

	for y in range(len(heightmap)):
		for x, letter in enumerate(heightmap[y]):
			if letter == 'S' or letter == 'a':
				startPositions += [(x, y)]
				letter = 'a'
			elif letter == 'E':
				endPosition = (x, y)
				letter = 'z'

			heights[y][x] = ord(letter)

	return (heights, startPositions, endPosition)

def computeDistances(heights, endPosition):
	maxY, maxX = len(heights), len(heights[0])
	queue = collections.deque([(endPosition)])
	distances = { endPosition: 0 }

	while queue:
		x, y = queue.popleft()

		for nx, ny in ((x + dx, y + dy) for dx, dy in DIRECTIONS):
			if 0 <= nx < maxX and 0 <= ny < maxY and heights[ny][nx] >= heights[y][x] - 1 and (nx, ny) not in distances:
				distances[(nx, ny)] = distances[(x, y)] + 1
				queue.append((nx, ny))

	return distances

def solve(heightmap):
	heights, startPositions, endPosition = parseMap(heightmap)
	distances = computeDistances(heights, endPosition)

	return min(distances[start] for start in startPositions if start in distances)


if __name__ == '__main__':
	heightmap = [list(line.strip()) for line in sys.stdin.readlines()]

	print(solve(heightmap))
