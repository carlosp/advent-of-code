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

def neighbours(x, y):
	return set([
		(x + 2, y),
		(x - 2, y),
		(x + 1, y + 1),
		(x + 1, y - 1),
		(x - 1, y + 1),
		(x - 1, y - 1)
	])

def iterate(blackTiles, n):
	for _ in range(n):
		allNeighbours = set()
		newBlackTiles = set(blackTiles)

		for x, y in blackTiles:
			n = neighbours(x, y)
			allNeighbours = allNeighbours | n
			adyacentBlackTiles = len(n & blackTiles)
			if adyacentBlackTiles == 0 or adyacentBlackTiles > 2:
				newBlackTiles.remove((x, y))

		for x, y in allNeighbours:
			n = neighbours(x, y)
			adyacentBlackTiles = len(n & blackTiles)
			if adyacentBlackTiles == 2:
				newBlackTiles.add((x, y))

		blackTiles = newBlackTiles

	return blackTiles

def solve(directionsList):
	blackTiles = computeBlackTiles(directionsList)
	blackTiles = iterate(blackTiles, 100)
	return len(blackTiles)


if __name__ == '__main__':
	print(solve(map(str.strip, sys.stdin.readlines())))
