#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

DIRECTIONS = {
	'R': (0, 1),
	'D': (1, 0),
	'L': (0, -1),
	'U': (-1, 0)
}

def areaByShoelace(corners):
	return abs(sum(
		(corners[idx - 1][0] + corners[idx][0]) * (corners[idx - 1][1] - corners[idx][1])
		for idx in range(len(corners))
	)) // 2

def computeLagoonVolume(digPlan):
	instructions = [(DIRECTIONS[direction], int(distance)) for direction, distance, _ in digPlan]
	corners, borderLength = [], 0
	row, col = 0, 0

	for (drow, dcol), distance in instructions:
		row, col = row + drow * distance, col + dcol * distance
		corners += [(row, col)]
		borderLength += distance

	return areaByShoelace(corners) + borderLength // 2 + 1


if __name__ == '__main__':
	digPlan = [line.split() for line in sys.stdin.readlines()]

	print(computeLagoonVolume(digPlan))
