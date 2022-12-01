#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(caloriesByElf, count):
	sortedSumOfCaloriesByElf = sorted(map(sum, caloriesByElf), reverse=True)

	return sum(sortedSumOfCaloriesByElf[:count])


if __name__ == '__main__':
	caloriesByElf = [
		list(map(int, lines.splitlines()))
		for lines in sys.stdin.read().split('\n' * 2)
	]

	print(solve(caloriesByElf, 1))
