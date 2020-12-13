#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

TARGET = 2020

def solve(numbers):
	setNumbers = set(numbers)
	assert len(numbers) == len(setNumbers), "All numbers should be distinct"

	for n1 in numbers:
		n2 = TARGET - n1
		if n1 != n2 and n2 in setNumbers:
			return n1 * n2


if __name__ == '__main__':
	numbers = list(map(int, sys.stdin.readlines()))
	print(solve(numbers))
