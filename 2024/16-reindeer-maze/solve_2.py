#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import math
import sys

def countTilesInBestPaths(maze: list[str]) -> int:
	tiles = { complex(row, col): maze[row][col] for row in range(len(maze)) for col in range(len(maze[row])) }
	position, direction = next(position for position in tiles if tiles[position] == 'S'), 1j
	bestCost, tilesInBestPaths = math.inf, set()
	visited, queue = {}, [(0, id := 0, position, direction, set())]

	while queue and queue[0][0] <= bestCost:
		cost, _, position, direction, path = heapq.heappop(queue)

		path.add(position)
		visited[(position, direction)] = cost

		if tiles[position] == 'E':
			bestCost = cost
			tilesInBestPaths.update(path)
			continue

		for nextCost, nextDirection in [(cost + 1, direction), (cost + 1001, direction * 1j), (cost + 1001, direction * -1j)]:
			if tiles[nextPosition := position + nextDirection] != '#' and (nextPosition, nextDirection) not in visited:
				heapq.heappush(queue, (nextCost, id := id + 1, nextPosition, nextDirection, path.copy()))

	return len(tilesInBestPaths)


if __name__ == '__main__':
	maze = list(map(str.strip, sys.stdin.readlines()))

	print(countTilesInBestPaths(maze))
