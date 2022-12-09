#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator
import sys

NUM_KNOTS = 2
MOVEMENTS = {
	'R': (1, 0),
	'L': (-1, 0),
	'U': (0, 1),
	'D': (0, -1)
}

def applyMovement(knots, movement):
	knots[0] = tuple(map(operator.add, knots[0], movement))

	for i in range(1, NUM_KNOTS):
		dx, dy = map(operator.sub, knots[i - 1], knots[i])

		if abs(dx) > 1 or abs(dy) > 1:
			knots[i] = tuple(map(operator.add, knots[i], (
				dx // abs(dx) if dx else 0,
				dy // abs(dy) if dy else 0
			)))

def countPositionsVisitedByTail(motions):
	knots = [(0, 0)] * NUM_KNOTS
	tailPositions = set([knots[-1]])

	for direction, numSteps in motions:
		for _ in range(numSteps):
			applyMovement(knots, MOVEMENTS[direction])
			tailPositions.add(knots[-1])

	return len(tailPositions)


if __name__ == '__main__':
	motions = [
		(direction, int(numSteps))
		for direction, numSteps in map(str.split, sys.stdin.readlines())
	]

	print(countPositionsVisitedByTail(motions))
