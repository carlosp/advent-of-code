#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import sys

class SnailfishNumber:
	@staticmethod
	def fromString(s):
		return SnailfishNumber._parse(eval(s))

	@staticmethod
	def _parse(value):
		if isinstance(value, int):
			return SnailfishLiteral(value)
		else:
			return SnailfishPair(*map(SnailfishNumber._parse, value))

	def _reduce(self):
		while True:
			if number := self._findNumberToExplode():
				number._explode()
			elif number := self._findNumberToSplit():
				number._split()
			else:
				break

		return self

	def _replace(self, other):
		other.parent = self.parent
		if self.parent.left == self:
			self.parent.left = other
		else:
			self.parent.right = other

	def __add__(self, other):
		return SnailfishPair(self.copy(), other.copy())._reduce()

class SnailfishPair(SnailfishNumber):
	def __init__(self, left, right):
		self.parent = None
		self.left = left
		self.right = right
		self.left.parent = self
		self.right.parent = self

	def copy(self):
		return SnailfishPair(self.left.copy(), self.right.copy())

	def magnitude(self):
		return 3 * self.left.magnitude() + 2 * self.right.magnitude()

	def _explode(self):
		self._incrementNext(False, self.left.value)
		self._incrementNext(True, self.right.value)
		self._replace(SnailfishLiteral(0))

	def _findNumberToExplode(self, depth=0):
		if depth == 4:
			return self
		elif (numberToExplode := self.left._findNumberToExplode(depth + 1)) or \
			(numberToExplode := self.right._findNumberToExplode(depth + 1)):
			return numberToExplode

	def _findNumberToSplit(self):
		if (numberToSplit := self.left._findNumberToSplit()) or \
			(numberToSplit := self.right._findNumberToSplit()):
			return numberToSplit

	def _incrementNext(self, forward, value):
		prev, next = lambda node: node.left, lambda node: node.right
		if not forward: prev, next = next, prev

		node = self
		while node.parent and node == next(node.parent):
			node = node.parent

		if node.parent:
			node = next(node.parent)
			while isinstance(node, SnailfishPair):
				node = prev(node)

			node.value += value

class SnailfishLiteral(SnailfishNumber):
	def __init__(self, value):
		self.value = value

	def copy(self):
		return SnailfishLiteral(self.value)

	def magnitude(self):
		return self.value

	def _findNumberToExplode(self, _):
		return None

	def _findNumberToSplit(self):
		if self.value >= 10:
			return self

	def _split(self):
		self._replace(SnailfishPair(
			SnailfishLiteral(self.value // 2),
			SnailfishLiteral((self.value + 1) // 2)
		))

def solve(numbers):
	return functools.reduce(lambda x, y: x + y, numbers).magnitude()

if __name__ == '__main__':
	numbers = list(map(SnailfishNumber.fromString, sys.stdin.readlines()))
	print(solve(numbers))
