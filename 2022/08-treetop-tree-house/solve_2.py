#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

def getHighestScenicScore(heights):
	def getViewingDistance(x, y, dx, dy):
		treeHouseHeight = heights[y][x]
		distance = 0

		while 1 <= x < numCols - 1 and 1 <= y < numRows - 1:
			x, y = x + dx, y + dy
			distance += 1

			if heights[y][x] >= treeHouseHeight:
				break

		return distance


	numRows, numCols = len(heights), len(heights[0])

	return max(
		math.prod((
			getViewingDistance(x, y, 1, 0),
			getViewingDistance(x, y, -1, 0),
			getViewingDistance(x, y, 0, 1),
			getViewingDistance(x, y, 0, -1)
		))
		for y in range(1, numRows - 1)
		for x in range(1, numCols - 1)
	)


if __name__ == '__main__':
	heights = [
		list(map(int, line.strip()))
		for line in sys.stdin.readlines()
	]

	print(getHighestScenicScore(heights))
