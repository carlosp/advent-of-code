#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

SCORING_CARD = {
	'X': { 'A': 3, 'B': 1, 'C': 2 },
	'Y': { 'A': 4, 'B': 5, 'C': 6 },
	'Z': { 'A': 8, 'B': 9, 'C': 7 }
}

def getGameScore(strategy):
	return sum([SCORING_CARD[b][a] for a, b in strategy])


if __name__ == '__main__':
	strategy = map(str.split, sys.stdin.readlines())

	print(getGameScore(strategy))
