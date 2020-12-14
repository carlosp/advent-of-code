#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(ratings):
	ratings = sorted(ratings)
	combs = [0] * (ratings[-1] + 1)

	combs[0] = 1
	for rating in ratings:
		combs[rating] = sum(combs[max(0, rating - 3):rating])

	return combs[-1]


if __name__ == '__main__':
	print(solve(list(map(int, sys.stdin.readlines()))))
