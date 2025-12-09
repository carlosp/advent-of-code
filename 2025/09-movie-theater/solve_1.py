#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys

Point = tuple[int, int]

def solve(redTiles: list[Point]) -> int:
	return max(
		(1 + abs(x2 - x1)) * (1 + abs(y2 - y1))
		for (x1, y1), (x2, y2) in itertools.combinations(redTiles, 2)
	)


if __name__ == '__main__':
	redTiles = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(solve(redTiles))
