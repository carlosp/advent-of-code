#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def getTrackPath(map: list[str]) -> list[tuple[int, int]]:
	height, width = len(map), len(map[0])
	startRow, startCol = next((row, col) for row in range(height) for col in range(width) if map[row][col] == 'S')
	queue, visited = [((startRow, startCol), [])], set([(startRow, startCol)])

	while queue:
		(row, col), path = queue.pop()

		path.append((row, col))

		if map[row][col] == 'E':
			return path

		for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nextRow, nextCol = row + drow, col + dcol

			if 0 <= nextRow < height and 0 <= nextCol < width and map[nextRow][nextCol] != '#' and (nextRow, nextCol) not in visited:
				visited.add((nextRow, nextCol))
				queue.append(((nextRow, nextCol), path))

def countCheats(map: list[str], cheatDuration: int, minSavedTime: int) -> int:
	height, width = len(map), len(map[0])
	distances = { (row, col): idx for idx, (row, col) in enumerate(getTrackPath(map)) }
	result = 0

	for distance, (row, col) in enumerate(distances):
		for row2 in range(max(row - cheatDuration, 0), min(row + cheatDuration + 1, height)):
			drow = abs(row2 - row)

			for col2 in range(max(col - (cheatDuration - drow), 0), min(col + cheatDuration - drow + 1, width)):
				if (distance2 := distances.get((row2, col2))) and distance2 - distance - (drow + abs(col2 - col)) >= minSavedTime:
					result += 1

	return result


if __name__ == '__main__':
	map = list(map(str.strip, sys.stdin.readlines()))

	print(countCheats(map, 20, 100))
