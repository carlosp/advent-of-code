#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
import collections
import sys

MAP_GUARD = '^'
MAP_OBSTACLE = '#'
START_GUARD_DIRECTION = (-1, 0)

def getPreviousObstacle(obstaclePositions: list[int], position: int) -> int | None:
	if (idx := bisect.bisect(obstaclePositions, position)) > 0:
		return obstaclePositions[idx - 1]

def getNextObstacle(obstaclePositions: list[int], position: int) -> int | None:
	if (idx := bisect.bisect(obstaclePositions, position)) < len(obstaclePositions):
		return obstaclePositions[idx]

def guardWillLoop(row: int, col: int, drow: int, dcol: int, obstaclesByRow: dict[int, list[int]], obstaclesByCol: dict[int, list[int]]) -> bool:
	visited = set()

	while (row, col, drow, dcol) not in visited:
		visited.add((row, col, drow, dcol))

		match drow, dcol:
			case (0, 1)  if (obstaclePosition := getNextObstacle(obstaclesByRow[row], col)) is not None		: col = obstaclePosition - 1
			case (0, -1) if (obstaclePosition := getPreviousObstacle(obstaclesByRow[row], col)) is not None	: col = obstaclePosition + 1
			case (1, 0)  if (obstaclePosition := getNextObstacle(obstaclesByCol[col], row)) is not None		: row = obstaclePosition - 1
			case (-1, 0) if (obstaclePosition := getPreviousObstacle(obstaclesByCol[col], row)) is not None	: row = obstaclePosition + 1
			case _: return False

		drow, dcol = dcol, -drow

	return True

def solve(map: list[str]) -> int:
	obstaclesByRow, obstaclesByCol = collections.defaultdict(list), collections.defaultdict(list)
	height, width = len(map), len(map[0])
	drow, dcol = START_GUARD_DIRECTION
	result = set()

	for row in range(height):
		for col in range(width):
			if map[row][col] == MAP_GUARD:
				startRow, startCol = currentRow, currentCol = row, col
			elif map[row][col] == MAP_OBSTACLE:
				bisect.insort(obstaclesByRow[row], col)
				bisect.insort(obstaclesByCol[col], row)

	while 0 <= (nextRow := currentRow + drow) < height and 0 <= (nextCol := currentCol + dcol) < width:
		if map[nextRow][nextCol] == MAP_OBSTACLE:
			drow, dcol = dcol, -drow
		else:
			obstaclesByRow[nextRow].insert(idx1 := bisect.bisect_left(obstaclesByRow[nextRow], nextCol), nextCol)
			obstaclesByCol[nextCol].insert(idx2 := bisect.bisect_left(obstaclesByCol[nextCol], nextRow), nextRow)

			if guardWillLoop(startRow, startCol, *START_GUARD_DIRECTION, obstaclesByRow, obstaclesByCol):
				result.add((nextRow, nextCol))

			obstaclesByRow[nextRow].pop(idx1)
			obstaclesByCol[nextCol].pop(idx2)
			currentRow, currentCol = nextRow, nextCol

	return len(result)


if __name__ == '__main__':
	map = list(map(str.strip, sys.stdin.readlines()))

	print(solve(map))
