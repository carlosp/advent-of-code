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

def waterRoughness(grid):
	isPartOfMonster = [[False] * len(grid[0]) for _ in range(len(grid))]
	monsterPattern = ['                  # ',
					  '#    ##    ##    ###',
					  ' #  #  #  #  #  #   ']

	for rowIdx in range(len(grid) - len(monsterPattern)):
		for colIdx in range(len(grid[0]) - len(monsterPattern[0])):
			isMonster = all(
				monsterPattern[mRowIdx][mColIdx] != '#' or grid[rowIdx + mRowIdx][colIdx + mColIdx] == '#'
				for mRowIdx in range(len(monsterPattern))
				for mColIdx in range(len(monsterPattern[0])))

			if isMonster:
				for mRowIdx in range(len(monsterPattern)):
					for mColIdx in range(len(monsterPattern[0])):
						if monsterPattern[mRowIdx][mColIdx] == '#':
							isPartOfMonster[rowIdx + mRowIdx][colIdx + mColIdx] = True


	return sum(grid[rowIdx][colIdx] == '#' and not isPartOfMonster[rowIdx][colIdx]
		for rowIdx in range(len(grid))
		for colIdx in range(len(grid[0])))

def buildFinalImage(orderedTiles):
	finalImage = []
	for tilesRow in orderedTiles:
		parts = []
		for orientedTile in tilesRow:
			parts += [[''.join(gridRow[1:-1]) for gridRow in orientedTile.grid[1:-1]]]

		finalImage += list(map(''.join, zip(*parts)))

	return finalImage

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

	finalImage = buildFinalImage(orderedTiles)

	return min(map(waterRoughness, allGridOrientations(finalImage)))


if __name__ == '__main__':
	rawTiles = list(map(lambda x: x.split('\n'), sys.stdin.read().strip().split('\n\n')))
	print(solve(rawTiles))
