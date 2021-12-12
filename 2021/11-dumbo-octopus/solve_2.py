#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

GRID_LENGTH = 10
DIRECTIONS = [
	(-1, -1), (-1, 0), (-1, 1),
	(0, -1), (0, 1),
	(1, -1), (1, 0), (1, 1)
]

def stepAndCountFlashes(energyLevels):
	def flash(x, y):
		energyLevels[x][y] += 1
		if energyLevels[x][y] == 10:
			allFlashes.append((x, y))
			pendingFlashes.append((x, y))


	allFlashes = []
	pendingFlashes = []

	for x in range(GRID_LENGTH):
		for y in range(GRID_LENGTH):
			flash(x, y)

	while pendingFlashes:
		x, y = pendingFlashes.pop()

		for nx, ny in [(x + dx, y + dy) for dx, dy in DIRECTIONS]:
			if 0 <= nx < GRID_LENGTH and 0 <= ny < GRID_LENGTH:
				flash(nx, ny)

	for x, y in allFlashes:
		energyLevels[x][y] = 0

	return len(allFlashes)

def solve(energyLevels):
	step = 1

	while stepAndCountFlashes(energyLevels) != GRID_LENGTH * GRID_LENGTH:
		step += 1

	return step


if __name__ == '__main__':
	energyLevels = [
		[int(energyLevel) for energyLevel in list(line.strip())]
		for line in sys.stdin.readlines()
	]
	print(solve(energyLevels))
