#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import sys

def countPlotsReachable(garden, steps):
	size, center = len(garden), len(garden) // 2
	pending, visited, reachable = [(center, center)], set(), 0

	for step in range(steps):
		nextPending = []

		for row, col in pending:
			for drow, dcol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				nextRow, nextCol = row + drow, col + dcol

				if garden[nextRow % size][nextCol % size] != '#' and (nextRow, nextCol) not in visited:
					visited.add((nextRow, nextCol))
					nextPending += [(nextRow, nextCol)]
					reachable += step % 2 != steps % 2

		pending, nextPending = nextPending, []

	return reachable

def solve(garden):
	size, center = len(garden), len(garden) // 2
	xValues = [0, 1, 2]
	yValues = [countPlotsReachable(garden, center + x * size) for x in xValues]

	return round(np.polyval(np.polyfit(xValues, yValues, 2), (26501365 - center) // size))


if __name__ == '__main__':
	garden = [line.strip() for line in sys.stdin.readlines()]

	print(solve(garden))
