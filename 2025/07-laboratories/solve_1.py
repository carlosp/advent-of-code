#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countSplits(manifold: list[str]) -> int:
	height, width = len(manifold), len(manifold[0])
	startPosition = next((row, col) for row in range(height) for col in range(width) if manifold[row][col] == 'S')
	newTachions, numSplits = { startPosition }, 0

	while tachions := newTachions:
		newTachions = set()

		for row, col in tachions:
			if row < height - 1:
				if manifold[row][col] == '^':
					newTachions.update([(row + 1, col - 1), (row + 1, col + 1)])
					numSplits += 1
				else:
					newTachions.add((row + 1, col))

	return numSplits


if __name__ == '__main__':
	manifold = list(map(str.strip, sys.stdin.readlines()))

	print(countSplits(manifold))
