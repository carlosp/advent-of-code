#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from itertools import starmap

UNIT_CONVERSION_ERROR = 10000000000000

def calculateMinTokensToWinAllPrizes(machines: list[tuple[int]]) -> int:
	def calculateMinTokensToWin(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> int:
		px += UNIT_CONVERSION_ERROR
		py += UNIT_CONVERSION_ERROR
		b = (ax * py - ay * px) // (ax * by - ay * bx)
		a = (px - b * bx) // ax

		return 3 * a + b if a * ax + b * bx == px and a * ay + b * by == py else 0


	return sum(starmap(calculateMinTokensToWin, machines))


if __name__ == '__main__':
	machines = [tuple(map(int, re.compile(r'\d+').findall(machine))) for machine in sys.stdin.read().split('\n\n')]

	print(calculateMinTokensToWinAllPrizes(machines))
