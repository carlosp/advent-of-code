#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from heapq import *

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def getMinRisk(riskLevels):
	baseSize = len(riskLevels)
	size = 5 * baseSize
	visited = set()
	q = [(0, 0, 0)]

	while True:
		currentCost, x, y = heappop(q)

		if x == size - 1 and y == x:
			return currentCost

		for nx, ny in ((x + dx, y + dy) for dx, dy in DIRECTIONS):
			if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited:
				cost = riskLevels[ny % baseSize][nx % baseSize] + ny // baseSize + nx // baseSize

				if cost >= 10:
					cost -= 9

				visited.add((nx, ny))
				heappush(q, (currentCost + cost, nx, ny))


if __name__ == '__main__':
	riskLevels = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

	print(getMinRisk(riskLevels))
