#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
PIPE_CONNECTIONS = collections.defaultdict(list, {
	'|': [N, S],
	'-': [E, W],
	'L': [N, E],
	'J': [N, W],
	'7': [S, W],
	'F': [S, E]
})

def getStartingPosition(grid):
	height, width = len(grid), len(grid[0])
	startRow, startCol = next((row, col) for row in range(height) for col in range(width) if grid[row][col] == 'S')
	pipeConnects = lambda row, col, dir: 0 <= row < height and 0 <= col < width and dir in PIPE_CONNECTIONS[grid[row][col]]

	startingPipeConnections = {
		(dr, dc)
		for dr, dc in [N, E, S, W]
		if pipeConnects(startRow + dr, startCol + dc, (-dr, -dc))
	}

	return startRow, startCol, next(pipe for pipe, connections in PIPE_CONNECTIONS.items() if set(connections) == startingPipeConnections)

def getLoopTiles(grid):
	startRow, startCol, startPipe = getStartingPosition(grid)
	loopTiles = set()

	grid[startRow][startCol] = startPipe
	queue = [(startRow, startCol)]

	while queue:
		row, col = queue.pop()
		loopTiles.add((row, col))

		for dr, dc in PIPE_CONNECTIONS[grid[row][col]]:
			if (nextTile := (row + dr, col + dc)) not in loopTiles:
				queue.append(nextTile)

	return loopTiles

def countStepsUntilFarthestPosition(grid):
	return len(getLoopTiles(grid)) // 2

if __name__ == '__main__':
	grid = [list(line.strip()) for line in sys.stdin.readlines()]

	print(countStepsUntilFarthestPosition(grid))
