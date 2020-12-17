#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys

DIMENSIONS = 4
ITERATIONS = 6
CELL_ACTIVE = '#'

def id(coordinates):
	return sum(x * pow(ITERATIONS * 3, idx) for idx, x in enumerate(coordinates))

NEIGHBOURS_IDS = [id(coordinates) for coordinates in itertools.product([-1, 0, 1], repeat=DIMENSIONS) if any(coordinates)]


def parseInitialState(initialGrid):
	return set(id([rowIdx, colIdx])
		for rowIdx in range(len(initialGrid))
		for colIdx in range(len(initialGrid[rowIdx]))
		if initialGrid[rowIdx][colIdx] == CELL_ACTIVE)

def getNeighbours(cellId):
	return set(cellId + neighbourId for neighbourId in NEIGHBOURS_IDS)

def solve(initialGrid):
	state = parseInitialState(initialGrid)

	for _ in range(ITERATIONS):
		newState = set()

		for cellId in set.union(*map(getNeighbours, state)):
			activeNeighbours = len(getNeighbours(cellId) & state)

			if cellId in state:
				if 2 <= activeNeighbours <= 3:
					newState.add(cellId)
			elif activeNeighbours == 3:
				newState.add(cellId)

		state = set(newState)

	return len(state)


if __name__ == '__main__':
	print(solve(list(map(str.strip, sys.stdin.readlines()))))
