#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def getTotalDistance(locationIds1: tuple[int, ...], locationIds2: tuple[int, ...]) -> int:
	return sum(
		abs(id1 - id2)
		for id1, id2
		in zip(sorted(locationIds1), sorted(locationIds2))
	)


if __name__ == '__main__':
	locationIds = [map(int, line.split()) for line in sys.stdin.readlines()]

	print(getTotalDistance(*zip(*locationIds)))
