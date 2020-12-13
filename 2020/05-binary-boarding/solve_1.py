#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

TO_BINARY = str.maketrans('FBLR', '0101')

def getSeatId(boardingPass):
	row = int(boardingPass[:7].translate(TO_BINARY), 2)
	col = int(boardingPass[7:].translate(TO_BINARY), 2)

	return row * 8 + col

if __name__ == '__main__':
	print(max(map(getSeatId, sys.stdin.readlines())))
