#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from itertools import count

HEIGHT, WIDTH = 103, 101
DISPLAY_EASTER_EGG = False

def calculateMinSecondsUntilEasterEgg(robots: list[tuple[int, int, int, int]]) -> int:
	for second in count(1):
		occupiedPositions = set()

		for idx, (x, y, dx, dy) in enumerate(robots):
			nextX, nextY = (x + dx) % WIDTH, (y + dy) % HEIGHT
			robots[idx] = (nextX, nextY, dx, dy)
			occupiedPositions.add((nextX, nextY))

		if len(robots) == len(occupiedPositions):
			DISPLAY_EASTER_EGG and print('\n'.join(
				''.join([' ', '#'][(col, row) in occupiedPositions] for col in range(WIDTH))
				for row in range(HEIGHT)
			))

			return second


if __name__ == '__main__':
	robots = [tuple(map(int, re.compile(r'-?\d+').findall(line))) for line in sys.stdin.readlines()]

	print(calculateMinSecondsUntilEasterEgg(robots))
