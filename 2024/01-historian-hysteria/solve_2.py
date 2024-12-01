#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

def getSimilarityScore(locationIds1: tuple[int, ...], locationIds2: tuple[int, ...]) -> int:
	locationIds2Count = collections.Counter(locationIds2)

	return sum(id1 * locationIds2Count[id1] for id1 in locationIds1)


if __name__ == '__main__':
	locationIds = [map(int, line.split()) for line in sys.stdin.readlines()]

	print(getSimilarityScore(*zip(*locationIds)))
