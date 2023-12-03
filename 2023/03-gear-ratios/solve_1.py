#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

NON_SYMBOL_CHARS = '0123456789.'

def hasAdjacentSymbol(engineSchematic, partRow, partColStart, partColEnd):
	return any(
		(gearRow, gearCol)
		for gearRow in [partRow - 1, partRow, partRow + 1]
		for gearCol in range(partColStart - 1, partColEnd + 1)
		if 0 <= gearRow < len(engineSchematic) and 0 <= gearCol < len(engineSchematic[gearRow])
			and engineSchematic[gearRow][gearCol] not in NON_SYMBOL_CHARS
	)

def getPartNumbers(engineSchematic):
	return [
		int(partMatch.group())
		for partRow in range(len(engineSchematic))
		for partMatch in re.finditer(r'\d+', engineSchematic[partRow])
		if hasAdjacentSymbol(engineSchematic, partRow, *partMatch.span())
	]


if __name__ == '__main__':
	engineSchematic = list(map(str.strip, sys.stdin.readlines()))

	print(sum(getPartNumbers(engineSchematic)))
