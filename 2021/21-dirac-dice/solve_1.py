#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

SCORE_TO_WIN = 1000
ROLLS = itertools.cycle([6, 5, 4, 3, 2, 1, 0, 9, 8, 7])

def solve(position1, position2):
	positions = [position1, position2]
	scores = [0, 0]

	for turn, roll in enumerate(ROLLS):
		player = turn % 2
		positions[player] = (positions[player] + roll - 1) % 10 + 1
		scores[player] += positions[player]

		if scores[player] >= SCORE_TO_WIN:
			return min(scores) * 3 * (turn + 1)


if __name__ == '__main__':
	position1 = int(input().split()[-1])
	position2 = int(input().split()[-1])

	print(solve(position1, position2))
