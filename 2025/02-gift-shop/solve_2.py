#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool

MAX_DIGITS_IN_ID = 10
PROPER_DIVISORS = {
	n: [(d, n // d) for d in range(1, n) if n % d == 0]
	for n in range(1, MAX_DIGITS_IN_ID + 1)
}

def isInvalidId(id: int) -> bool:
	strId = str(id)

	for prefixLen, factor in PROPER_DIVISORS[len(strId)]:
		if strId[:prefixLen] * factor == strId:
			return True

def getSumOfInvalidIds(startId: int, endId: int) -> int:
	return sum(id for id in range(startId, endId + 1) if isInvalidId(id))


if __name__ == '__main__':
	productIdRanges = [tuple(map(int, strRange.split('-'))) for strRange in input().split(',')]

	with Pool() as pool:
		print(sum(pool.starmap(getSumOfInvalidIds, productIdRanges)))
