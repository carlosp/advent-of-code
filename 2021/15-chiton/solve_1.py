#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from heapq import *

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def getMinRisk(riskLevels):
	size = len(riskLevels)
	visited = set()
	q = [(0, 0, 0)]

	while True:
		currentCost, x, y = heappop(q)

		if x == size - 1 and y == x:
			return currentCost

		for nx, ny in ((x + dx, y + dy) for dx, dy in DIRECTIONS):
			if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited:
				visited.add((nx, ny))
				heappush(q, (currentCost + riskLevels[ny][nx], nx, ny))


if __name__ == '__main__':
	riskLevels = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

	print(getMinRisk(riskLevels))
