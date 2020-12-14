#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MOVE_NORTH = 'N'
MOVE_SOUTH = 'S'
MOVE_EAST = 'E'
MOVE_WEST = 'W'
MOVE_FORWARD = 'F'
TURN_LEFT = 'L'
TURN_RIGHT = 'R'

class Point(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def translate(self, vector, times=1):
		self._x += times * vector.x()
		self._y += times * vector.y()

	def x(self):
		return self._x

	def y(self):
		return self._y


class Vector(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def add(self, x, y):
		self._x += x
		self._y += y

	def rot(self, angle):
		assert angle % 90 == 0, 'can only rotate in multiples of 90 degrees'

		quarters = (angle // 90) % 4
		if quarters == 1:
			self._x, self._y = self._y, -self._x
		elif quarters == 2:
			self._x, self._y = -self._x, -self._y
		elif quarters == 3:
			self._x, self._y = -self._y, self._x

	def x(self):
		return self._x

	def y(self):
		return self._y


class Ship(object):
	def __init__(self):
		self._pos = Point(0, 0)
		self._dir = Vector(1, 0)

	def pos(self):
		return self._pos

	def moveNorth(self, value):
		self._pos.translate(Vector(0, value))

	def moveSouth(self, value):
		self._pos.translate(Vector(0, -value))

	def moveEast(self, value):
		self._pos.translate(Vector(value, 0))

	def moveWest(self, value):
		self._pos.translate(Vector(-value, 0))

	def moveForward(self, value):
		self._pos.translate(self._dir, value)

	def turnLeft(self, value):
		self._dir.rot(-value)

	def turnRight(self, value):
		self._dir.rot(value)


def solve(instructions):
	s = Ship()

	for op, value in map(lambda x: (x[0], int(x[1:])), instructions):
		if op == MOVE_NORTH:
			s.moveNorth(value)
		elif op == MOVE_SOUTH:
			s.moveSouth(value)
		elif op == MOVE_EAST:
			s.moveEast(value)
		elif op == MOVE_WEST:
			s.moveWest(value)
		elif op == MOVE_FORWARD:
			s.moveForward(value)
		elif op == TURN_LEFT:
			s.turnLeft(value)
		elif op == TURN_RIGHT:
			s.turnRight(value)

	return abs(s.pos().x()) + abs(s.pos().y())


if __name__ == '__main__':
	print(solve(map(str.strip, sys.stdin.readlines())))
