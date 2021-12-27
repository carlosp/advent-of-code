#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countStepsUntilStopMoving(seafloor):
	def move(positionsToMove, dx, dy):
		newPositions, hasMoved = set(), False

		for x, y in positionsToMove:
			nextPosition = ((x + dx) % width, (y + dy) % height)

			if nextPosition not in eastFacing and nextPosition not in southFacing:
				newPositions.add(nextPosition)
				hasMoved = True
			else:
				newPositions.add((x, y))

		return hasMoved, newPositions


	height, width = len(seafloor), len(seafloor[0])
	eastFacing = { (x, y) for y in range(height) for x in range(width) if seafloor[y][x] == '>' }
	southFacing = { (x, y) for y in range(height) for x in range(width) if seafloor[y][x] == 'v' }
	step, movedEast, movedSouth = 0, True, True

	while movedEast or movedSouth:
		step += 1
		movedEast, eastFacing = move(eastFacing, 1, 0)
		movedSouth, southFacing = move(southFacing, 0, 1)

	return step


if __name__ == '__main__':
	seafloor = [line.strip() for line in sys.stdin.readlines()]
	print(countStepsUntilStopMoving(seafloor))
