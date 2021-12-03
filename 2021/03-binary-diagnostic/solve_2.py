#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

BIT_ZERO = '0'
BIT_ONE = '1'

def applyBitCriteria(numbers, criteria):
	position = 0
	while len(numbers) > 1:
		numbersWithBit0 = list(filter(lambda number: number[position] == BIT_ZERO, numbers))
		numbersWithBit1 = list(filter(lambda number: number[position] == BIT_ONE, numbers))
		numbers = criteria(numbersWithBit0, numbersWithBit1)
		position += 1

	return numbers[0]

def getLifeSupportRating(numbers):
	oxigenGeneratorRating = applyBitCriteria(numbers, lambda numbersWithBit0, numbersWithBit1:
		numbersWithBit1 if len(numbersWithBit1) >= len(numbersWithBit0) else numbersWithBit0)
	co2ScrubberRating = applyBitCriteria(numbers, lambda numbersWithBit0, numbersWithBit1:
		numbersWithBit0 if len(numbersWithBit0) <= len(numbersWithBit1) else numbersWithBit1)

	return int(oxigenGeneratorRating, 2) * int(co2ScrubberRating, 2)


if __name__ == '__main__':
	numbers = list(map(str.strip, sys.stdin.readlines()))
	print(getLifeSupportRating(numbers))
