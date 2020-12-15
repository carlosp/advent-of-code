#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import array

ITERATIONS = 30000000

def solve(numbers):
	lastTurns = array.array('i', [-1] * ITERATIONS)
	previousLastTurns = array.array('i', [-1] * ITERATIONS)
	lastNumberSpoken = None
	x, y = -1, -1

	for idx in range(ITERATIONS):
		if idx < len(numbers):
			lastNumberSpoken = numbers[idx]
		elif x == -1:
			lastNumberSpoken = 0
		else:
			lastNumberSpoken = y - x

		y = lastTurns[lastNumberSpoken]
		previousLastTurns[lastNumberSpoken] = y
		lastTurns[lastNumberSpoken] = idx
		x, y = y, idx

	return lastNumberSpoken


if __name__ == '__main__':
	print(solve(list(map(int, input().split(',')))))
