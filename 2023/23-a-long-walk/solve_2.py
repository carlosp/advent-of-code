#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
NEIGHBOUR_DIRECTIONS = [N, E, S, W]

class Node(object):
	def __init__(self, position):
		self.position = position
		self.neighbours = []
		self.visited = False


def buildGraph(grid, start, end):
	height, width = len(grid), len(grid[0])
	nodes = {
		start: Node(start),
		end: Node(end)
	}
	queue = [(nodes[start], start[0] + 1, start[1], 1)]

	while queue:
		fromNode, row, col, distance = queue.pop()

		if grid[row][col] == '#':
			continue

		if node := nodes.get((row, col), None):
			fromNode.neighbours += [(node, distance)]
			node.neighbours += [(fromNode, distance)]
			continue

		neighbours = []
		for drow, dcol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nextRow = row + drow
			nextCol = col + dcol

			if 0 <= nextRow < height and 0 <= nextCol < width and grid[nextRow][nextCol] != '#' and \
				(nextRow, nextCol) != fromNode.position:

				neighbours += [(nextRow, nextCol)]

		if len(neighbours) == 1:
			grid[row][col] = '#'
			queue += [(fromNode, *neighbours[0], distance + 1)]
		else:
			newNode = Node((row, col))

			nodes[(row, col)] = newNode
			fromNode.neighbours += [(newNode, distance)]
			newNode.neighbours += [(fromNode, distance)]
			queue += [(newNode, *neighbour, 1) for neighbour in neighbours]

	return nodes


def calculateLongestPath(node, endNode, distance):
	if node == endNode:
		return distance

	node.visited = True
	result = 0

	for nextNode, nextDistance in node.neighbours:
		if not nextNode.visited:
			result = max(result, calculateLongestPath(nextNode, endNode, distance + nextDistance))

	node.visited = False

	return result

def solve(grid):
	start = 0, next(col for col in range(len(grid[0])) if grid[0][col] == '.')
	end = len(grid) - 1, next(col for col in range(len(grid[0])) if grid[-1][col] == '.')
	nodes = buildGraph(grid, start, end)

	return calculateLongestPath(nodes[start], nodes[end], 0)


if __name__ == '__main__':
	grid = [list(line.strip()) for line in sys.stdin.readlines()]

	print(solve(grid))
