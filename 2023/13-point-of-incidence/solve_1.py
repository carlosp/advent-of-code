#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def summarizeReflection(lines, line):
	before, after = line, line + 1

	while before >= 0 and after < len(lines):
		if lines[before] != lines[after]:
			return 0

		before -= 1
		after += 1

	return line + 1

def summarizePattern(rows, cols, exclude=None):
	for lines, multiplier in [(rows, 100), (cols, 1)]:
		for line in range(len(lines) - 1):
			if (summary := multiplier * summarizeReflection(lines, line)) and summary != exclude:
				return summary

def solve(pattern):
	width = len(pattern[0])
	rows = [[row[col] == '.' for col in range(width)] for row in pattern]
	cols = [[row[col] == '.' for row in pattern] for col in range(width)]

	return summarizePattern(rows, cols)


if __name__ == '__main__':
	print(sum(
		solve(list(map(list, block.splitlines())))
		for block in sys.stdin.read().split('\n' * 2)
	))
