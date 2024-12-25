#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countFittingLockKeyPairs(schematics: list[list[str]]) -> int:
	height, width = len(schematics[0]), len(schematics[0][0])
	locks, keys = [], []

	for schematic in schematics:
		if schematic[0].startswith('.'):
			keys.append([
				next(height - row - 1 for row in range(1, height) if schematic[row][col] == '#')
				for col in range(width)
			])
		else:
			locks.append([
				next(row - 1 for row in range(1, height) if schematic[row][col] == '.')
				for col in range(width)
			])

	return sum(
		all(key[idx] + lock[idx] <= height - 2 for idx in range(width))
		for key in keys
		for lock in locks
	)


if __name__ == '__main__':
	schematics = list(lines.splitlines() for lines in sys.stdin.read().split('\n\n'))

	print(countFittingLockKeyPairs(schematics))
