#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(assignments):
	return sum(
		1 for start1, end1, start2, end2 in assignments
		if start1 <= start2 <= end2 <= end1 or start2 <= start1 <= end1 <= end2
	)


if __name__ == '__main__':
	assignments = [
		map(int, line.replace('-', ' ').replace(',', ' ').split())
		for line in sys.stdin.readlines()
	]

	print(solve(assignments))
