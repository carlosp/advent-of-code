#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool

def isInvalidId(id: int) -> bool:
	strId = str(id)

	return strId[:len(strId) // 2] == strId[len(strId) // 2:]

def getSumOfInvalidIds(startId: int, endId: int) -> int:
	return sum(id for id in range(startId, endId + 1) if isInvalidId(id))


if __name__ == '__main__':
	productIdRanges = [tuple(map(int, strRange.split('-'))) for strRange in input().split(',')]

	with Pool() as pool:
		print(sum(pool.starmap(getSumOfInvalidIds, productIdRanges)))
