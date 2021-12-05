#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import re
import sys

def countOverlappingPoints(segments):
	slope = lambda a, b: (b - a) / max(1, abs(b - a))
	pointCounts = collections.Counter()

	for x1, y1, x2, y2 in segments:
		dx = slope(x1, x2)
		dy = slope(y1, y2)
		length = max(abs(x2 - x1), abs(y2 - y1))

		pointCounts.update((x1 + i * dx, y1 + i * dy) for i in range(length + 1))

	return sum(1 for count in pointCounts.values() if count > 1)


if __name__ == '__main__':
	segments = [
		map(int, digits)
		for digits in map(re.compile(r'\d+').findall, sys.stdin.readlines())
	]
	print(countOverlappingPoints(segments))
