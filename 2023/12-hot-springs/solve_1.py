#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from functools import cache

NUM_COPIES = 1

def countPossibleArrangements(springs, sizes):
	@cache
	def count(springIdx, sizesIdx, damaged):
		if springIdx == len(springs):
			return (sizesIdx == len(sizes) - 1 and sizes[sizesIdx] == damaged) or \
				(not damaged and sizesIdx == len(sizes))

		if sizesIdx == len(sizes):
			return '#' not in springs[springIdx:]

		if damaged > sizes[sizesIdx]:
			return 0

		result = 0

		if springs[springIdx] != '.':
			result += count(springIdx + 1, sizesIdx, damaged + 1)

		if springs[springIdx] != '#':
			if sizes[sizesIdx] == damaged:
				result += count(springIdx + 1, sizesIdx + 1, 0)
			elif not damaged:
				result += count(springIdx + 1, sizesIdx, damaged)

		return result

	return count(0, 0, 0)


if __name__ == '__main__':
	print(sum(
		countPossibleArrangements('?'.join([record] * NUM_COPIES), NUM_COPIES * tuple(map(int, sizes.split(','))))
		for record, sizes in [line.split() for line in sys.stdin.readlines()]
	))
