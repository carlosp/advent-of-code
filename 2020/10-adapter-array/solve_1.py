#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(ratings):
	ratings = [0] + sorted(ratings)
	differences = [b - a for a, b in zip(ratings, ratings[1:])]

	return differences.count(1) * (differences.count(3) + 1)


if __name__ == '__main__':
	print(solve(list(map(int, sys.stdin.readlines()))))
