#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

TO_BINARY = str.maketrans('FBLR', '0101')

def getSeatId(boardingPass):
	row = int(boardingPass[:7].translate(TO_BINARY), 2)
	col = int(boardingPass[7:].translate(TO_BINARY), 2)

	return row * 8 + col

def solve(boardingPasses):
	seatIds = sorted(map(getSeatId, boardingPasses))

	for i in range(1, len(seatIds)):
		if seatIds[i] != seatIds[i - 1] + 1:
			return seatIds[i] - 1


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
