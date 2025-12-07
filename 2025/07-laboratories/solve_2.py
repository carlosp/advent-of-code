#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

def countTimelines(manifold: list[str]) -> int:
	height, width = len(manifold), len(manifold[0])
	startPosition = next((row, col) for row in range(height) for col in range(width) if manifold[row][col] == 'S')
	newTachions, timelinesInPosition = { startPosition }, collections.defaultdict(int, { startPosition: 1 })

	while tachions := newTachions:
		newTachions = set()

		for row, col in tachions:
			if row < height - 1:
				numTimelines = timelinesInPosition[(row, col)]

				if manifold[row][col] == '^':
					newTachions.update([(row + 1, col - 1), (row + 1, col + 1)])
					timelinesInPosition[(row + 1, col - 1)] += numTimelines
					timelinesInPosition[(row + 1, col + 1)] += numTimelines
				else:
					newTachions.add((row + 1, col))
					timelinesInPosition[(row + 1, col)] += numTimelines

	return sum(timelinesInPosition[(height - 1, col)] for col in range(width))


if __name__ == '__main__':
	manifold = list(map(str.strip, sys.stdin.readlines()))

	print(countTimelines(manifold))
