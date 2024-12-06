#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MAP_GUARD = '^'
MAP_OBSTACLE = '#'
START_GUARD_DIRECTION = (-1, 0)

def solve(map: list[str]) -> int:
	height, width = len(map), len(map[0])
	drow, dcol = START_GUARD_DIRECTION
	result = set()

	for row in range(height):
		for col in range(width):
			if map[row][col] == MAP_GUARD:
				currentRow, currentCol = row, col

	while 0 <= (nextRow := currentRow + drow) < height and 0 <= (nextCol := currentCol + dcol) < width:
		if map[nextRow][nextCol] == MAP_OBSTACLE:
			drow, dcol = dcol, -drow
		else:
			result.add((currentRow, currentCol))
			currentRow, currentCol = nextRow, nextCol

	return len(result) + 1


if __name__ == '__main__':
	map = list(map(str.strip, sys.stdin.readlines()))

	print(solve(map))
