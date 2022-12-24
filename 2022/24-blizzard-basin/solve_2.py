#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import math
import sys

BLIZZARD_DIRECTIONS = {
	'^': (0, -1),
	'>': (1, 0),
	'v': (0, 1),
	'<': (-1, 0)
}
POSSIBLE_MOVEMENTS = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

def generateBlizzardsCycle(valley):
	def moveBlizzards(blizzards):
		newBlizzards = collections.defaultdict(list)

		for (x, y), blizzardDirections in blizzards.items():
			for dx, dy in blizzardDirections:
				nx, ny = x + dx, y + dy

				if nx == 0:             nx = width - 2
				elif nx == width - 1:   nx = 1
				elif ny == 0:           ny = height - 2
				elif ny == height - 1:  ny = 1

				newBlizzards[(nx, ny)].append((dx, dy))

		return newBlizzards


	height, width = len(valley), len(valley[0])
	blizzards = {
		(x, y) : [BLIZZARD_DIRECTIONS[valley[y][x]]]
		for y in range(height)
		for x in range(width)
		if valley[y][x] in BLIZZARD_DIRECTIONS
	}
	blizzardsCycle = []

	for _ in range(math.lcm(height - 2, width - 2)):
		blizzardsCycle.append(blizzards)
		blizzards = moveBlizzards(blizzards)

	return blizzardsCycle

def minTimeForTrip(valley, blizzardsCycle, startTime, startPosition, endPosition):
	q = collections.deque([(startTime, startPosition)])
	visited = set()

	while q:
		time, (x, y) = q.popleft()

		if (x, y) == endPosition:
			return time

		if (x, y) not in blizzardsCycle[time % len(blizzardsCycle)]:
			for dx, dy in POSSIBLE_MOVEMENTS:
				nx, ny = x + dx, y + dy
				nextState = (time + 1, (nx, ny))

				if ny < len(valley) and valley[ny][nx] != '#' and nextState not in visited:
					visited.add(nextState)
					q.append(nextState)


def solve(valley):
	blizzardsCycle = generateBlizzardsCycle(valley)
	startPosition = (valley[0].index('.'), 0)
	endPosition = (valley[-1].index('.'), len(valley) - 1)

	time1 = minTimeForTrip(valley, blizzardsCycle, 0, startPosition, endPosition)
	time2 = minTimeForTrip(valley, blizzardsCycle, time1, endPosition, startPosition)
	return minTimeForTrip(valley, blizzardsCycle, time2, startPosition, endPosition)


if __name__ == '__main__':
	valley = list(map(str.strip, sys.stdin.readlines()))

	print(solve(valley))
