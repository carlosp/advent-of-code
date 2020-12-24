#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def computeBlackTiles(directionsList):
	blackTiles = set()

	for directions in directionsList:
		x, y, idx = 0, 0, 0

		while idx < len(directions):
			if directions[idx] == 'e':
				x, y = x + 2, y
			elif directions[idx] == 'w':
				x, y = x - 2, y
			else:
				y += 1 if directions[idx] == 'n' else -1
				x += 1 if directions[idx + 1] == 'e' else -1
				idx += 1

			idx += 1

		if (x, y) in blackTiles:
			blackTiles.remove((x, y))
		else:
			blackTiles.add((x, y))

	return blackTiles

def solve(directionsList):
	blackTiles = computeBlackTiles(directionsList)
	return len(blackTiles)


if __name__ == '__main__':
	print(solve(map(str.strip, sys.stdin.readlines())))
