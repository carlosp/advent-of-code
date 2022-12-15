#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def countPositionsThatCannotContainBeacon(report, y):
	result = set()

	for sx, sy, bx, by in report:
		distance = abs(sx - bx) + abs(sy - by)
		dx = distance - abs(sy - y)
		result.update(range(sx - dx, sx + dx + 1))

	result -= { bx for _, _, bx, by in report if by == y }

	return len(result)


if __name__ == '__main__':
	report = [
		tuple(map(int, re.findall(r'-?\d+', line)))
		for line in sys.stdin.readlines()
	]

	print(countPositionsThatCannotContainBeacon(report, 2000000))
