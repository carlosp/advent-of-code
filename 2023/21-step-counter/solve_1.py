#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countPlotsReachable(garden, steps):
	size, center = len(garden), len(garden) // 2
	pending, visited, reachable = [(center, center)], set(), 0

	for step in range(steps):
		nextPending = []

		for row, col in pending:
			for drow, dcol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				nextRow, nextCol = row + drow, col + dcol

				if 0 <= nextRow < size and 0 <= nextCol < size and garden[nextRow][nextCol] != '#' and (nextRow, nextCol) not in visited:
					visited.add((nextRow, nextCol))
					nextPending += [(nextRow, nextCol)]
					reachable += step % 2 != steps % 2

		pending, nextPending = nextPending, []

	return reachable


if __name__ == '__main__':
	garden = [line.strip() for line in sys.stdin.readlines()]

	print(countPlotsReachable(garden, 64))
