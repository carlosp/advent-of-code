#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys

TARGET = 2020

def solve(numbers):
	setNumbers = set(numbers)
	assert len(numbers) == len(setNumbers), "All numbers should be distinct"

	for n1, n2 in itertools.combinations(numbers, 2):
		n3 = TARGET - n1 - n2
		if n1 != n3 and n2 != n3 and n3 in setNumbers:
			return n1 * n2 * n3


if __name__ == '__main__':
	numbers = list(map(int, sys.stdin.readlines()))
	print(solve(numbers))
