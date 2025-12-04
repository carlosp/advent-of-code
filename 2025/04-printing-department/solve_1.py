#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

ADJACENT_DIRECTIONS = [-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j]

def isRollAccessible(rolls: set[complex], roll: complex) -> bool:
	adjacents = { roll + direction for direction in ADJACENT_DIRECTIONS }

	return len(rolls & adjacents) < 4

def countAccessibleRolls(grid: list[str]) -> int:
	rolls = { complex(row, col) for row in range(len(grid)) for col in range(len(grid[row])) if grid[row][col] == '@' }

	return sum(isRollAccessible(rolls, roll) for roll in rolls)


if __name__ == '__main__':
	grid = [line.strip() for line in sys.stdin.readlines()]

	print(countAccessibleRolls(grid))
