#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)

def countEnergizedTiles(grid, size, row, col, dir):
	pending, seen = [(row, col, dir)], set()

	while pending:
		row, col, (drow, dcol) = state = pending.pop()

		if 0 <= row < size and 0 <= col < size and state not in seen:
			seen.add(state)

			match grid[row][col]:
				case '.': pending += [(row + drow, col + dcol, (drow, dcol))]
				case '/': pending += [(row - dcol, col - drow, (-dcol, -drow))]
				case '\\': pending += [(row + dcol, col + drow, (dcol, drow))]
				case '-': pending += [(row, col + 1, E), (row, col - 1, W)]
				case '|': pending += [(row - 1, col, N), (row + 1, col, S)]

	return len(set((row, col) for row, col, _ in seen))


def solve(grid):
	size = len(grid)

	return(max(
		max(
			countEnergizedTiles(grid, size, idx, 0, E),
			countEnergizedTiles(grid, size, idx, size - 1, W),
			countEnergizedTiles(grid, size, 0, idx, S),
			countEnergizedTiles(grid, size, size - 1, idx, N)
		)
		for idx in range(size)
	))


if __name__ == '__main__':
	grid = [line.strip() for line in sys.stdin.readlines()]

	print(solve(grid))
