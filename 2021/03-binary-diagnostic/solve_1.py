#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

BIT_ZERO = '0'
BIT_ONE = '1'

def getPowerConsumption(numbers):
	gammaRate, epsilonRate = '', ''

	for position in range(len(numbers[0])):
		count0s = len(list(filter(lambda number: number[position] == BIT_ZERO, numbers)))
		count1s = len(list(filter(lambda number: number[position] == BIT_ONE, numbers)))
		gammaRate += BIT_ONE if count1s > count0s else BIT_ZERO
		epsilonRate += BIT_ONE if count1s < count0s else BIT_ZERO

	return int(gammaRate, 2) * int(epsilonRate, 2)


if __name__ == '__main__':
	numbers = list(map(str.strip, sys.stdin.readlines()))
	print(getPowerConsumption(numbers))
