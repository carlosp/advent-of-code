#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def countWaysToBeatRecord(time, bestDistance):
	x = int(math.sqrt(time * time - 4 * bestDistance) - time) // -2
	return time - 1 - 2 * x


if __name__ == '__main__':
	time = int(''.join(input().split(':')[1].split()))
	bestDuration = int(''.join(input().split(':')[1].split()))

	print(countWaysToBeatRecord(time, bestDuration))
