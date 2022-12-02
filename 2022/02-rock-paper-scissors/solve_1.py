#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

SCORING_CARD = {
	'X': { 'A': 4, 'B': 1, 'C': 7 },
	'Y': { 'A': 8, 'B': 5, 'C': 2 },
	'Z': { 'A': 3, 'B': 9, 'C': 6 }
}

def getGameScore(strategy):
	return sum([SCORING_CARD[b][a] for a, b in strategy])


if __name__ == '__main__':
	strategy = map(str.split, sys.stdin.readlines())

	print(getGameScore(strategy))
