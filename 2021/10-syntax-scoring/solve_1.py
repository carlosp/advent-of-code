#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

CLOSING_TO_OPENING_PAIR = { closing: opening for opening, closing in ['()', '[]', '{}', '<>'] }
ERROR_SCORES = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

def getSyntaxErrorScore(line):
	stack = []

	for char in line:
		if char not in CLOSING_TO_OPENING_PAIR:
			stack.append(char)
		elif not stack or stack.pop() != CLOSING_TO_OPENING_PAIR[char]:
			return ERROR_SCORES[char]

	return 0

def solve(lines):
	return sum(map(getSyntaxErrorScore, lines))


if __name__ == '__main__':
	lines = list(map(str.strip, sys.stdin.readlines()))
	print(solve(lines))
