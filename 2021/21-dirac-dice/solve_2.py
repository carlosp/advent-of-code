#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import cache

SCORE_TO_WIN = 21
ROLL_FREQUENCIES = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

@cache
def countWins(position1, position2, score1, score2):
	if score2 >= SCORE_TO_WIN:
		return (0, 1)

	result1, result2 = 0, 0
	for roll, frequency in ROLL_FREQUENCIES:
		position = (position1 + roll - 1) % 10 + 1
		wins2, wins1 = countWins(position2, position, score2, score1 + position)
		result1 += frequency * wins1
		result2 += frequency * wins2

	return result1, result2

def solve(position1, position2):
	return max(countWins(position1, position2, 0, 0))


if __name__ == '__main__':
	position1 = int(input().split()[-1])
	position2 = int(input().split()[-1])

	print(solve(position1, position2))
