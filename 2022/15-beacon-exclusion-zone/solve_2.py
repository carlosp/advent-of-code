#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

DISTRESS_BEACON_MAX_COORD = 4000000

def getTuningFrequency(report):
	intervalsWithoutBeaconByRow = [[] for _ in range(DISTRESS_BEACON_MAX_COORD + 1)]

	for sx, sy, bx, by in report:
		distance = abs(sx - bx) + abs(sy - by)
		minY = min(max(sy - distance, 0), DISTRESS_BEACON_MAX_COORD)
		maxY = min(max(sy + distance, 0), DISTRESS_BEACON_MAX_COORD)

		for y in range(minY, maxY + 1):
			dx = distance - abs(sy - y)
			intervalsWithoutBeaconByRow[y].append((sx - dx, sx + dx))

	for y, intervalsWithoutBeacon in enumerate(intervalsWithoutBeaconByRow):
		x = -1
		for startX, endX in sorted(intervalsWithoutBeacon):
			if startX == x + 2:
				return 4000000 * (x + 1) + y

			x = max(x, endX)


if __name__ == '__main__':
	report = [
		tuple(map(int, re.findall(r'-?\d+', line)))
		for line in sys.stdin.readlines()
	]

	print(getTuningFrequency(report))
