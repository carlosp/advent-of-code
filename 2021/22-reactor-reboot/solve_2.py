#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import re
import sys

class Cuboid:
	def __init__(self, minX, maxX, minY, maxY, minZ, maxZ):
		self.minX, self.maxX = minX, maxX
		self.minY, self.maxY = minY, maxY
		self.minZ, self.maxZ = minZ, maxZ

	def __and__(self, other):
		if self.minX > other.maxX or other.minX > self.maxX or \
			self.minY > other.maxY or other.minY > self.maxY or \
			self.minZ > other.maxZ or other.minZ > self.maxZ:

			return Cuboid.EMPTY

		return Cuboid(
			max(self.minX, other.minX), min(self.maxX, other.maxX),
			max(self.minY, other.minY), min(self.maxY, other.maxY),
			max(self.minZ, other.minZ), min(self.maxZ, other.maxZ)
		)

	def __sub__(self, other):
		if (common := self & other) == Cuboid.EMPTY:
			return [self]
		else:
			possibleCuboids = [
				Cuboid(self.minX, common.minX - 1, self.minY, self.maxY, self.minZ, self.maxZ),
				Cuboid(common.maxX + 1, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ),
				Cuboid(common.minX, common.maxX, self.minY, common.minY - 1, self.minZ, self.maxZ),
				Cuboid(common.minX, common.maxX, common.maxY + 1, self.maxY, self.minZ, self.maxZ),
				Cuboid(common.minX, common.maxX, common.minY, common.maxY, self.minZ, common.minZ - 1),
				Cuboid(common.minX, common.maxX, common.minY, common.maxY, common.maxZ + 1, self.maxZ)
			]
			return [cuboid for cuboid in possibleCuboids
					if cuboid.minX <= cuboid.maxX and cuboid.minY <= cuboid.maxY and cuboid.minZ <= cuboid.maxZ]

	def volume(self):
		return (self.maxX - self.minX + 1) * (self.maxY - self.minY + 1) * (self.maxZ - self.minZ + 1)


Cuboid.EMPTY = Cuboid(*([0] * 6))

def countActiveCubes(instructions):
	activeCuboids = []

	for mode, cuboid in instructions:
		activeCuboids = itertools.chain(
			[cuboid] if mode == 'on' else [],
			*(activeCuboid - cuboid for activeCuboid in activeCuboids)
		)

	return sum(cuboid.volume() for cuboid in activeCuboids)


if __name__ == '__main__':
	instructions = []

	for line in sys.stdin.readlines():
		mode = line.split()[0]
		cuboid = Cuboid(*[int(digits) for digits in re.compile(r'-?\d+').findall(line)])
		instructions += [(mode, cuboid)]

	print(countActiveCubes(instructions))
