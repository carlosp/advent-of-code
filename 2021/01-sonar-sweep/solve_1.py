#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

WINDOW_SIZE = 1

def solve(depths):
	return sum(
		1 if depths[idx] > depths[idx - WINDOW_SIZE] else 0
		for idx in range(WINDOW_SIZE, len(depths))
	)

if __name__ == '__main__':
	depths = list(map(int, sys.stdin.readlines()))
	print(solve(depths))
