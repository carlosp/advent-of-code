#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

type Coordinate = tuple[int, int]

def getTrailheadRating(map: list[list[int]], row: int, col: int, cache: dict[Coordinate, int]) -> int:
	def dfs(row: int, col: int) -> int:
		if map[row][col] == 9:
			return 1
		elif (cacheKey := (row, col)) not in cache:
			result = 0

			for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				nextRow, nextCol = row + drow, col + dcol

				if 0 <= nextRow < len(map) and 0 <= nextCol < len(map[0]) and map[nextRow][nextCol] == 1 + map[row][col]:
					result += dfs(nextRow, nextCol)

			cache[cacheKey] = result

		return cache[cacheKey]

	return dfs(row, col)


def solve(map: list[list[int]]) -> int:
	cache = {}

	return sum(
		getTrailheadRating(map, row, col, cache)
		for row in range(len(map))
		for col in range(len(map[0]))
		if map[row][col] == 0
	)


if __name__ == '__main__':
	map = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

	print(solve(map))
