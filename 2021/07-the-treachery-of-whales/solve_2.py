#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getMinFuelToAlignPositions(positions):
	fuelNeeded = lambda distance: distance * (distance + 1) // 2

	return min(map(
		lambda target: sum(fuelNeeded(abs(position - target)) for position in positions),
		range(min(positions), max(positions) + 1)
	))


if __name__ == '__main__':
	positions = list(map(int, input().split(',')))
	print(getMinFuelToAlignPositions(positions))
