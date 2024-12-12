#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N, S, E, W = 1, -1, 1j, -1j

def calculateAreas(map: dict[complex, str]) -> dict[complex, int]:
	def fill(position: complex) -> None:
		pending, visited = [position], set()

		while pending:
			visited.add(position := pending.pop())

			for direction in [N, S, E, W]:
				if map[position] == map.get(nextPosition := position + direction) and nextPosition not in visited:
					pending.append(nextPosition)

		for position in visited:
			areas[position] = len(visited)

		return areas


	areas = {}

	for position in map:
		if position not in areas:
			fill(position)

	return areas

def calculateTopFencePricesForSegment(map: dict[complex, str], areas: dict[complex, int], position: complex, direction: complex) -> int:
	above = lambda position: position + direction * 1j
	result = 0

	while position in map:
		if map[position] != map[above(position)]:
			while (nextPosition := position + direction) in map and map[position] == map[nextPosition] != map[above(nextPosition)]:
				position = nextPosition

			result += areas[position]
		position += direction

	return result

def calculateFencingPrice(map: list[str]) -> int:
	height, width = len(map), len(map[0])
	paddedMap = {
		complex(row, col): map[row - 1][col - 1] if 1 <= row <= height and 1 <= col <= width else ''
		for row in range(height + 2)
		for col in range(width + 2)
	}
	areas = calculateAreas(paddedMap)

	return (
		sum(calculateTopFencePricesForSegment(paddedMap, areas, complex(row + 1, 1), E) for row in range(height)) +
		sum(calculateTopFencePricesForSegment(paddedMap, areas, complex(row + 1, width), W) for row in range(height)) +
		sum(calculateTopFencePricesForSegment(paddedMap, areas, complex(1, col + 1), N) for col in range(width)) +
		sum(calculateTopFencePricesForSegment(paddedMap, areas, complex(width, col + 1), S) for col in range(width))
	)


if __name__ == '__main__':
	map = list(map(str.strip, sys.stdin.readlines()))

	print(calculateFencingPrice(map))
