#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

WINDOW_SIZE = 25

def findFirstNumberNotSumOfTwoPreviousInWindow(numbers):
	numbersInWindow = collections.defaultdict(int)

	for number in numbers[:WINDOW_SIZE]:
		numbersInWindow[number] += 1

	for idx in range(WINDOW_SIZE, len(numbers)):
		number, found = numbers[idx], False

		for n1 in numbers[idx - WINDOW_SIZE:idx]:
			n2 = number - n1
			if numbersInWindow[n2] > (n1 == n2):
				found = True
				break

		if not found:
			return number

		numbersInWindow[numbers[idx - WINDOW_SIZE]] -= 1
		numbersInWindow[number] += 1

def findEncryptionWeakness(numbers, target):
	sum, end = 0, 0

	for start in range(len(numbers)):
		while sum < target:
			sum += numbers[end]
			end = end + 1

		if sum == target:
			sortedNumbers = sorted(numbers[start:end])
			return sortedNumbers[0] + sortedNumbers[-1]

		end -= 1
		sum = sum - numbers[start] - numbers[end]


def solve(numbers):
	target = findFirstNumberNotSumOfTwoPreviousInWindow(numbers)
	return findEncryptionWeakness(numbers, target)


if __name__ == '__main__':
	print(solve(list(map(int, sys.stdin.readlines()))))
