#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

if sys.version_info < (3, 8):
	sys.exit('python 3.8+ required')


def chinese_remainder(mods, remainders):
	sum = 0
	nprod = math.prod(mods)

	for n, a in zip(mods, remainders):
		y = nprod // n
		sum += a * y * pow(y, -1, n)

	return sum % nprod

def solve(earliestDepart, buses):
	constraints = {int(bus): int(bus) - idx for idx, bus in enumerate(buses) if bus != 'x'}

	return chinese_remainder(constraints.keys(), constraints.values())


if __name__ == '__main__':
	earliestDepart = int(input())
	buses = input().split(',')
	print(solve(earliestDepart, buses))
