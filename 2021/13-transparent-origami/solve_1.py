#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

NEW_LINE = '\n'

def applyFolds(dots, folds):
	for axis, pos in folds:
		if axis == 'x':
			dots = {(min(x, 2 * int(pos) - x), y) for x, y in dots}
		else:
			dots = {(x, min(y, 2 * int(pos) - y)) for x, y in dots}

	return dots

def solve(dots, folds):
	dots = applyFolds(dots, folds[:1])

	return len(dots)


if __name__ == '__main__':
	dotsInput, foldsInput = sys.stdin.read().split(NEW_LINE * 2)
	dots = {tuple(map(int, line.split(','))) for line in dotsInput.split(NEW_LINE)}
	folds = [line.split(' ')[-1].split('=') for line in foldsInput.split(NEW_LINE)]

	print(solve(dots, folds))
