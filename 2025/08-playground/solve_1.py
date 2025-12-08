#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
import sys
from typing import Generic, TypeVar

T = TypeVar('T')

class DisjointSet(Generic[T]):
	class Node[T]:
		def __init__(self, value: T) -> None:
			self.value = value
			self.parent = self
			self.size = 1


	def __init__(self, values: list[T]) -> None:
		self.nodes = { value: DisjointSet.Node(value) for value in values }

	def find(self, value: T) -> Node[T]:
		node = self.nodes[value]

		while node.parent is not node:
			node.parent = node.parent.parent
			node = node.parent

		return node

	def merge(self, value1: T, value2: T) -> int:
		node1, node2 = self.find(value1), self.find(value2)

		if node1 != node2:
			if node1.size < node2.size:
				node1, node2 = node2, node1

			node2.parent = node1
			node1.size += node2.size

		return node1.size


def solve(positions: list[tuple[int, int, int]], numConnections: int) -> int:
	disjointSet = DisjointSet[tuple[int, int, int]](positions)
	shortestPairs = sorted((math.dist(pos1, pos2), pos1, pos2) for pos1, pos2 in itertools.combinations(positions, 2))

	for _, pos1, pos2 in shortestPairs[:numConnections]:
		disjointSet.merge(pos1, pos2)

	return math.prod(
		node.size for node in
		sorted(set(map(disjointSet.find, positions)), key=lambda node: node.size)[-3:]
	)


if __name__ == '__main__':
	positions = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(solve(positions, 1000))
