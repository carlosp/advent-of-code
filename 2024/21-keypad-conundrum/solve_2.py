#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from functools import cache
from itertools import pairwise

KEYPAD_DIRECTIONS = {
	1: 'v',
	-1: '^',
	1j: '>',
	-1j: '<'
}
NUMERIC_KEYPAD = ('789', '456', '123', ' 0A')
DIRECTIONAL_KEYPAD = (' ^A', '<v>')

@cache
def getKeypadDirections(keypad: tuple[str], fromButton: str, toButton: str) -> list[str]:
	buttons = { complex(row, col): keypad[row][col] for row in range(len(keypad)) for col in range(len(keypad[row])) if keypad[row][col] != ' ' }
	startPosition = next(position for position in buttons if buttons[position] == fromButton)
	queue, visited, paths = [(startPosition, KEYPAD_DIRECTIONS.keys(), '')], set(), []

	while queue:
		position, possibleDirections, path = queue.pop(0)

		visited.add(position)

		if buttons[position] == toButton:
			paths.append(path)
			continue

		for direction in possibleDirections:
			steps = 1

			while (nextPosition := position + steps * direction) in buttons and nextPosition not in visited:
				queue.append((nextPosition, possibleDirections - set([direction]), path + steps * KEYPAD_DIRECTIONS[direction]))
				steps += 1

	return paths

@cache
def calculateShortestSequence(code: str, keypad: tuple[str], numRobots: int) -> int:
	if numRobots == 0:
		return len(code)
	else:
		return sum(
			min(
				calculateShortestSequence(possiblePath + 'A', DIRECTIONAL_KEYPAD, numRobots - 1)
				for possiblePath in getKeypadDirections(keypad, previousButton, nextButton)
			)
			for previousButton, nextButton in pairwise('A' + code)
		)

def calculateSumOfComplexities(codes: list[str], numRobots: int) -> int:
	return sum(
		int(code[:-1]) * calculateShortestSequence(code, NUMERIC_KEYPAD, numRobots)
		for code in codes
	)


if __name__ == '__main__':
	codes = list(map(str.strip, sys.stdin.readlines()))

	print(calculateSumOfComplexities(codes, 1 + 25))
