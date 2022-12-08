#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countVisibleTrees(heights):
	def markVisibleTrees(x, y, dx, dy):
		maxHeight = -1

		while 0 <= x < numCols and 0 <= y < numRows:
			if heights[y][x] > maxHeight:
				visible[y][x] = True
				maxHeight = heights[y][x]

			x, y = x + dx, y + dy


	numRows, numCols = len(heights), len(heights[0])
	visible = [[False] * numCols for _ in range(numRows)]

	for y in range(numRows):
		markVisibleTrees(0, y, 1, 0)
		markVisibleTrees(numCols - 1, y, -1, 0)

	for x in range(numCols):
		markVisibleTrees(x, 0, 0, 1)
		markVisibleTrees(x, numRows - 1, 0, -1)

	return sum(map(sum, visible))


if __name__ == '__main__':
	heights = [
		list(map(int, line.strip()))
		for line in sys.stdin.readlines()
	]

	print(countVisibleTrees(heights))
