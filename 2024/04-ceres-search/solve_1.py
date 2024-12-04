#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def extractWord(grid: list[str], row: int, col: int, drow: int, dcol: int, length: int) -> str | None:
	if 0 <= row + (length - 1) * drow < len(grid) and 0 <= col + (length - 1) * dcol < len(grid[0]):
		return ''.join(grid[row + i * drow][col + i * dcol] for i in range(length))

def countXmas(grid: list[str]) -> int:
	height, width = len(grid), len(grid[0])
	result = 0

	for row in range(height):
		for col in range(width):
			for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
				result += extractWord(grid, row, col, drow, dcol, 4) == 'XMAS'

	return result


if __name__ == '__main__':
	grid = list(map(str.strip, sys.stdin.readlines()))

	print(countXmas(grid))
