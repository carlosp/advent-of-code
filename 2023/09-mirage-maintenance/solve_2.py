#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def extrapolatePreviousValue(history):
	diffs = [history[idx] - history[idx - 1] for idx in range(1, len(history))]

	return history[0] - (diffs[0] if len(set(diffs)) == 1 else extrapolatePreviousValue(diffs))


if __name__ == '__main__':
	print(sum(
		extrapolatePreviousValue(history)
		for history in (list(map(int, line.split())) for line in sys.stdin.readlines())
	))
