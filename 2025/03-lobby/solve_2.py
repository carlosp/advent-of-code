#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def calculateMaxJoltage(joltageRatings: list[int], numBatteries: int) -> int:
	if numBatteries == 1:
		return max(joltageRatings)
	elif numBatteries == len(joltageRatings):
		return int(''.join(map(str, joltageRatings)))

	largestAvailable = max(joltageRatings[:len(joltageRatings) - numBatteries + 1])
	firstLargestIdx = joltageRatings.index(largestAvailable)

	return largestAvailable * 10**(numBatteries - 1) + \
		calculateMaxJoltage(joltageRatings[firstLargestIdx + 1:], numBatteries - 1)

def calculateTotalOutputJoltage(banks: list[list[int]], joltageOutputSize: int) -> int:
	return sum(calculateMaxJoltage(joltageRatings, joltageOutputSize) for joltageRatings in banks)


if __name__ == '__main__':
	banks = [
		[int(joltageRating) for joltageRating in line.strip()]
		for line in sys.stdin.readlines()
	]

	print(calculateTotalOutputJoltage(banks, 12))
