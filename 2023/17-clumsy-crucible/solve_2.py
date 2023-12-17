#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import sys

def computeMinHeatLoss(grid, minStepsStraight, maxStepsStraight):
	height, width = len(grid), len(grid[0])
	pending, seen = [(0, 0, 0, 0, 1), (0, 0, 0, 1, 0)], {}

	while pending:
		dist, row, col, drow, dcol = heapq.heappop(pending)

		if row == height - 1 and col == width - 1:
			return dist

		for nextDirRow, nextDirCol in [(dcol, drow), (-dcol, -drow)]:
			nextRow, nextCol, nextDist = row, col, dist

			for steps in range(1, maxStepsStraight + 1):
				nextRow += nextDirRow
				nextCol += nextDirCol

				if 0 <= nextRow < height and 0 <= nextCol < width:
					nextDist += grid[nextRow][nextCol]
					nextState = (nextRow, nextCol, nextDirRow, nextDirCol)

					if steps >= minStepsStraight and nextDist < seen.get(nextState, 2**64):
						seen[nextState] = nextDist
						heapq.heappush(pending, (nextDist, *nextState))
				else:
					break


if __name__ == '__main__':
	grid = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

	print(computeMinHeatLoss(grid, 4, 10))
