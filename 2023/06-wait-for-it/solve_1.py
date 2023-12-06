#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def countWaysToBeatRecord(time, bestDistance):
	x = int(math.sqrt(time * time - 4 * bestDistance) - time) // -2
	return time - 1 - 2 * x


if __name__ == '__main__':
	times = map(int, input().split(':')[1].split())
	bestDurations = map(int, input().split(':')[1].split())

	print(math.prod(
		countWaysToBeatRecord(time, bestDuration)
		for time, bestDuration in zip(times, bestDurations))
	)
