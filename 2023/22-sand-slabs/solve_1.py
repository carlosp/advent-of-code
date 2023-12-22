#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

class Brick(object):
	def __init__(self, start, end):
		self.startX, self.startY, self.startZ = start
		self.endX, self.endY, self.endZ = end
		self.bottom = min(self.startZ, self.endZ)
		self.top = max(self.startZ, self.endZ)
		self.isSupportOf = set()
		self.isSupportedBy = set()

	def overlapsVertically(self, other):
		return other.startX <= self.endX and other.endX >= self.startX and \
			other.startY <= self.endY and other.endY >= self.startY

	def drop(self, distance):
		self.startZ -= distance
		self.endZ -= distance
		self.bottom -= distance
		self.top -= distance


def settle(bricks):
	bricks.sort(key=lambda brick: brick.bottom)

	for idx, brick in enumerate(bricks):
		settleDistance = min((
			brick.bottom - other.top
			for other in bricks[:idx]
			if brick.overlapsVertically(other)),
			default=brick.bottom
		) - 1
		brick.drop(settleDistance)

	for idx, brick in enumerate(bricks):
		for other in bricks[:idx]:
			if brick.overlapsVertically(other) and brick.bottom == other.top + 1:
				brick.isSupportedBy.add(other)
				other.isSupportOf.add(brick)

def solve(bricks):
	settle(bricks)

	criticalBricks = { brick for brick in bricks if any(len(other.isSupportedBy) == 1 for other in brick.isSupportOf) }

	return len(bricks) - len(criticalBricks)


if __name__ == '__main__':
	bricks = [
		Brick(*(list(map(int, point.split(','))) for point in line.split('~')))
		for line in sys.stdin.readlines()
	]

	print(solve(bricks))
