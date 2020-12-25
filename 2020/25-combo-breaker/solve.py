#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = 20201227

def calculateLoopSize(pk):
	loopSize, value = 0, 1

	while value != pk:
		loopSize += 1
		value = (value * 7) % N

	return loopSize

def transform(subject, loopSize):
	value = 1

	for _ in range(loopSize):
		value = (value * subject) % N

	return value

def solve(cardPk, doorPk):
	cardLoopSize = calculateLoopSize(cardPk)
	return transform(doorPk, cardLoopSize)


if __name__ == '__main__':
	print(solve(int(input()), int(input())))
