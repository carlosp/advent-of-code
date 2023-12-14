#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

CYCLE_TILT_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
NUM_CYCLES = 1000000000

def tilt(grid, height, width, direction, roundedRocks):
	drow, dcol = direction
	newRoundedRocks = []

	for row, col in roundedRocks:
		startRow, startCol = row, col
		movedDistance = 0

		while True:
			row, col = row + drow, col + dcol

			if row < 0 or row == height or col < 0 or col == width or grid[row][col] == '#':
				break

			movedDistance += (row, col) not in roundedRocks

		newRoundedRocks += [(startRow + drow * movedDistance, startCol + dcol * movedDistance)]

	return frozenset(newRoundedRocks)

def computeTotalLoad(grid):
	height, width = len(grid), len(grid[0])
	roundedRocks = frozenset([(row, col) for row in range(height) for col in range(width) if grid[row][col] == 'O'])
	seenStates = {}

	for cycle in range(NUM_CYCLES):
		seenStates[roundedRocks] = cycle

		for direction in CYCLE_TILT_DIRECTIONS:
			roundedRocks = tilt(grid, height, width, direction, roundedRocks)

		if previousCycle := seenStates.get(roundedRocks):
			cycleLength = (cycle + 1) - previousCycle
			remainingCycles = (NUM_CYCLES - cycle - 1) % cycleLength
			roundedRocks = next(state for state, cycle in seenStates.items() if cycle == previousCycle + remainingCycles)
			break

	return sum(height - row for row, _ in roundedRocks)


if __name__ == '__main__':
	grid = [list(line.strip()) for line in sys.stdin.readlines()]

	print(computeTotalLoad(grid))
