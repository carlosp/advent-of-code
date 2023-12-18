#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

DIRECTIONS = {
	'0': (0, 1),
	'1': (1, 0),
	'2': (0, -1),
	'3': (-1, 0)
}

def areaByShoelace(corners):
	return abs(sum(
		(corners[idx - 1][0] + corners[idx][0]) * (corners[idx - 1][1] - corners[idx][1])
		for idx in range(len(corners))
	)) // 2

def computeLagoonVolume(digPlan):
	instructions = [(DIRECTIONS[color[-2]], int(color[2:7], 16)) for _, _, color in digPlan]
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
