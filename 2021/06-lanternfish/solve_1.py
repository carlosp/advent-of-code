#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections

def countLanternfishes(initialAges, numDays):
	ageCounts = collections.deque([0] * 9)

	for age in initialAges:
		ageCounts[age] += 1

	for _ in range(numDays):
		ageCounts.rotate(-1)
		ageCounts[6] += ageCounts[-1]

	return sum(ageCounts)


if __name__ == '__main__':
	ages = map(int, input().split(','))
	print(countLanternfishes(ages, 80))
