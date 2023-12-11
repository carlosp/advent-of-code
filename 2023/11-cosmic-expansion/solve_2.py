#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
import sys

EXPANSION_FACTOR = 999999

def parseImage(image):
	height, width = len(image), len(image[0])
	emptyRows, emptyCols = set(range(height)), set(range(width))
	galaxies = []

	for row in range(height):
		for col in range(width):
			if image[row][col] == '#':
				emptyRows.discard(row)
				emptyCols.discard(col)
				galaxies += [(row, col)]

	return sorted(emptyRows), sorted(emptyCols), galaxies

def solve(image):
	emptyRows, emptyCols, galaxies = parseImage(image)
	result = 0

	for idx, (row1, col1) in enumerate(galaxies):
		for (row2, col2) in galaxies[idx + 1:]:
			minCol, maxCol = min(col1, col2), max(col1, col2)
			result += EXPANSION_FACTOR * (
				bisect.bisect_right(emptyRows, row2) - bisect.bisect_left(emptyRows, row1) +
				bisect.bisect_right(emptyCols, maxCol) - bisect.bisect_left(emptyCols, minCol)
			) + (row2 - row1) + (maxCol - minCol)

	return result


if __name__ == '__main__':
	image = [line.strip() for line in sys.stdin.readlines()]

	print(solve(image))
