#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import math
import re
import sys

GEAR_SYMBOL = '*'

def getAdjacentGears(engineSchematic, partRow, partColStart, partColEnd):
	return [
		(gearRow, gearCol)
		for gearRow in [partRow - 1, partRow, partRow + 1]
		for gearCol in range(partColStart - 1, partColEnd + 1)
		if 0 <= gearRow < len(engineSchematic) and 0 <= gearCol < len(engineSchematic[gearRow])
			and engineSchematic[gearRow][gearCol] == GEAR_SYMBOL
	]

def getGearRatios(engineSchematic):
	potentialGears = collections.defaultdict(list)

	for partRow in range(len(engineSchematic)):
		for partMatch in re.finditer(r'\d+', engineSchematic[partRow]):
			for gear in getAdjacentGears(engineSchematic, partRow, *partMatch.span()):
				potentialGears[gear].append(int(partMatch.group()))

	return [
		math.prod(partNumbers)
		for _, partNumbers in potentialGears.items()
		if len(partNumbers) == 2
	]


if __name__ == '__main__':
	engineSchematic = list(map(str.strip, sys.stdin.readlines()))

	print(sum(getGearRatios(engineSchematic)))
