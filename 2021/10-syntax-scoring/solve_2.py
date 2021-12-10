#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

CLOSING_TO_OPENING_PAIR = { closing: opening for opening, closing in ['()', '[]', '{}', '<>'] }
POINTS_TRANSLATION = str.maketrans('([{<', '1234')

def getCompletionScore(line):
	stack = []

	for char in line:
		if char not in CLOSING_TO_OPENING_PAIR:
			stack.append(char)
		elif not stack or stack.pop() != CLOSING_TO_OPENING_PAIR[char]:
			return 0

	return int(''.join(reversed(stack)).translate(POINTS_TRANSLATION), 5)

def solve(lines):
	completionScores = sorted([score for score in map(getCompletionScore, lines) if score])
	return completionScores[len(completionScores) // 2]


if __name__ == '__main__':
	lines = list(map(str.strip, sys.stdin.readlines()))
	print(solve(lines))
