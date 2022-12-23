#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)
NE = (1, -1)
NW = (-1, -1)
SE = (1, 1)
SW = (-1, 1)
ALL_DIRECTIONS = [N, S, E, W, NE, NW, SE, SW]
LOOK_ORDER = collections.deque([
	(N, [N, NE, NW]),
	(S, [S, SE, SW]),
	(W, [W, NW, SW]),
	(E, [E, NE, SE])
])

def simulateRound(currentPositions):
	newPositions, proposedNewPositions = set(), collections.defaultdict(list)

	for x, y in currentPositions:
		newPosition = None

		if any((x + dx, y + dy) in currentPositions for dx, dy in ALL_DIRECTIONS):
			for (moveX, moveY), directionsToCheck in LOOK_ORDER:
				if all((x + dx, y + dy) not in currentPositions for dx, dy in directionsToCheck):
					newPosition = (x + moveX, y + moveY)
					proposedNewPositions[newPosition].append((x, y))
					break

		if not newPosition:
			newPositions.add((x, y))

	for newPosition, oldPositions in proposedNewPositions.items():
		if len(oldPositions) == 1:
			newPositions.add(newPosition)
		else:
			newPositions.update(oldPositions)

	LOOK_ORDER.rotate(-1)

	return newPositions

def solve(grove):
	positions = { (x, y) for y in range(len(grove)) for x in range(len(grove[y])) if grove[y][x] == '#' }

	for _ in range(10):
		positions = simulateRound(positions)

	minX = min(x for x, _ in positions)
	maxX = max(x for x, _ in positions)
	minY = min(y for _, y in positions)
	maxY = max(y for _, y in positions)

	return (maxX - minX + 1) * (maxY - minY + 1) - len(positions)


if __name__ == '__main__':
	grove = list(map(str.strip, sys.stdin.readlines()))

	print(solve(grove))
