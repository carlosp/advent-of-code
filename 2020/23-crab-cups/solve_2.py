#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

CUPS = 1000000
ITERATIONS = 10000000

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class CupsHolder(object):
	def __init__(self, cups):
		self._nodes = [None] * (CUPS + 1)

		last = Node(cups[0])
		self._nodes[cups[0]] = last

		for cup in cups[1:]:
			current = Node(cup)
			self._nodes[cup] = current
			last.next = current
			last = current

		self._current = self._nodes[cups[0]]
		last.next = self._current

	def iterate(self, n):
		for _ in range(n):
			destination = self._current.value - 1
			if destination == 0:
				destination = CUPS

			while destination == self._current.next.value or \
					destination == self._current.next.next.value or \
					destination == self._current.next.next.next.value:

				destination -= 1
				if destination == 0:
					destination = CUPS

			destinationNode = self._nodes[destination]
			tmp = destinationNode.next
			destinationNode.next = self._current.next
			self._current.next = self._current.next.next.next.next
			destinationNode.next.next.next.next = tmp
			self._current = self._current.next

	def result(self):
		return self._nodes[1].next.value * self._nodes[1].next.next.value


def solve(cups):
	cupsHolder = CupsHolder(cups + [i for i in range(10, CUPS + 1)])
	cupsHolder.iterate(ITERATIONS)
	return cupsHolder.result()


if __name__ == '__main__':
	print(solve(list(map(int, sys.stdin.read()))))
