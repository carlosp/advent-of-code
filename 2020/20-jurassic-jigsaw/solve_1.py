#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

class OrientedTile(object):
	def __init__(self, id, grid):
		self.id = id
		self.grid = grid
		self.top = ''.join(grid[0][col] for col in range(len(grid)))
		self.right = ''.join(grid[row][-1] for row in range(len(grid)))
		self.bottom = ''.join(grid[-1][col] for col in range(len(grid)))
		self.left = ''.join(grid[row][0] for row in range(len(grid)))


def allGridRotations(grid):
	rotate = lambda x, y: (y, len(grid) - 1 - x)
	rotations = [grid]

	for _ in range(3):
		newGrid = [[None] * len(grid) for _ in range(len(grid))]

		for rowIdx in range(len(grid)):
			for colIdx in range(len(grid)):
				x, y = rotate(rowIdx, colIdx)
				newGrid[x][y] = rotations[-1][rowIdx][colIdx]

		rotations += [newGrid]

	return rotations

def allGridOrientations(grid):
	return allGridRotations(grid) + allGridRotations(grid[::-1])

def arrange(orientedTileMap, usedTiles, grid, row, col):
	for tileId, orientedTiles in orientedTileMap.items():
		if tileId in usedTiles:
			continue

		usedTiles.add(tileId)

		for orientedTile in orientedTiles:
			if row > 0 and orientedTile.top != grid[row - 1][col].bottom:
					continue

			if col > 0 and orientedTile.left != grid[row][col - 1].right:
					continue

			grid[row][col] = orientedTile

			if arrange(orientedTileMap, usedTiles, grid, row + (col // (len(grid) - 1)), (col + 1) % len(grid)):
				return True

		usedTiles.remove(tileId)

	return row == len(grid)

def solve(rawTiles):
	size = int(math.sqrt(len(rawTiles)))
	orderedTiles = [[None] * size for _ in range(size)]
	orientedTileMap = {}

	for rawTile in rawTiles:
		tileId = int(rawTile[0].split(' ')[1][:-1])
		orientedTileMap[tileId] = list(map(
			lambda grid: OrientedTile(tileId, grid),
			allGridOrientations(rawTile[1:])))

	assert arrange(orientedTileMap, set(), orderedTiles, 0, 0) == True

	return orderedTiles[0][0].id * orderedTiles[0][-1].id * orderedTiles[-1][0].id * orderedTiles[-1][-1].id


if __name__ == '__main__':
	rawTiles = list(map(lambda x: x.split('\n'), sys.stdin.read().strip().split('\n\n')))
	print(solve(rawTiles))
