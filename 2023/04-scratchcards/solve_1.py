#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countPoints(scratchcard):
	winningNumbers, myNumbers = map(set, map(str.split, scratchcard.split(':')[1].split('|')))
	myWinningNumbers = winningNumbers & myNumbers

	return 2 ** (len(myWinningNumbers) - 1) if myWinningNumbers else 0


if __name__ == '__main__':
	print(sum(map(countPoints, sys.stdin.readlines())))
