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
			if grid[row][col] == 'A' and 0 < row < height - 1 and 0 < col < width - 1:
				result += all([
					extractWord(grid, row - 1, col - 1, 1, 1, 3) in ('MAS', 'SAM'),
					extractWord(grid, row - 1, col + 1, 1, -1, 3) in ('MAS', 'SAM')
				])

	return result


if __name__ == '__main__':
	grid = list(map(str.strip, sys.stdin.readlines()))

	print(countXmas(grid))
