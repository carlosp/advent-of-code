#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import re

MAX_STEPS = 160

def getPossibleVelocitiesToReachTarget(minX, maxX, minY, maxY):
	possibleVxBySteps = collections.defaultdict(list)
	possibleVelocities = set()

	for vx in range(maxX + 1):
		x, dx = 0, vx

		for step in range(1, MAX_STEPS):
			x += dx
			dx = max(0, dx - 1)

			if minX <= x <= maxX:
				possibleVxBySteps[step].append(vx)

	for vy in range(minY, max(-minY, maxY)):
		y, dy = 0, vy

		for step in range(1, MAX_STEPS):
			y += dy
			dy -= 1

			if minY <= y <= maxY:
				possibleVelocities.update((vx, vy) for vx in possibleVxBySteps[step])

	return possibleVelocities

def getHighestPossibleAltitude(*args):
	maxVy = max(vy for _, vy in getPossibleVelocitiesToReachTarget(*args))

	return maxVy * (maxVy + 1) // 2


if __name__ == '__main__':
	numbers = [int(digits) for digits in re.compile(r'-?\d+').findall(input())]

	print(getHighestPossibleAltitude(*numbers))
