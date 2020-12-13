#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(groups):
	total = 0

	for group in groups:
		total += len(set.intersection(*map(set, group.replace('\n', ' ').strip().split(' '))))

	return total


if __name__ == '__main__':
	print(solve(sys.stdin.read().split('\n\n')))
