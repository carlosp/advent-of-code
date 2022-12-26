#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import operator
import re
import sys

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Face(object):
	def __init__(self, grid, boardPosition):
		self.grid = grid
		self.boardPosition = boardPosition
		self.connections = {}

	def connect(self, direction, otherFace):
		self.connections[direction] = otherFace

class Cube(object):
	def __init__(self, board):
		self.board = board
		self.sideLength = math.gcd(len(board), max(len(row) for row in board))
		self.faces = {}
		self.topLeftFace = None

		for x in range(0, len(board[0]), self.sideLength):
			if face := self._parseFace((x, 0)):
				self.topLeftFace = face
				break

		self._wrapFaces()

	def _parseFace(self, position):
		if position not in self.faces:
			boardX, boardY = position

			if 0 <= boardY < len(self.board) and 0 <= boardX < len(self.board[boardY]) and self.board[boardY][boardX] != ' ':
				faceGrid = [row[boardX:boardX + self.sideLength] for row in self.board[boardY:boardY + self.sideLength]]
				self.faces[position] = face = Face(faceGrid, (boardX, boardY))

				for (dx, dy) in DIRECTIONS:
					if otherFace := self._parseFace((boardX + dx * self.sideLength, boardY + dy * self.sideLength)):
						face.connect((dx, dy), otherFace)
						otherFace.connect((-dx, -dy), face)

				return face

	def _wrapFaces(self):
		for face in self.faces.values():
			for (dx, dy) in DIRECTIONS:
				if (dx, dy) not in face.connections:
					nextFace = face
					while (-dx, -dy) in nextFace.connections:
						nextFace = nextFace.connections[(-dx, -dy)]

					face.connect((dx, dy), nextFace)
					nextFace.connect((-dx, -dy), face)

class Position(object):
	def __init__(self, cube, face, start, facing):
		self.cube = cube
		self.face = face
		self.x, self.y = start
		self.dx, self.dy = facing

	def getPassword(self):
		boardX, boardY = tuple(map(operator.add, self.face.boardPosition, (self.x + 1, self.y + 1)))

		return 1000 * boardY + 4 * boardX + [(1, 0), (0, 1), (-1, 0), (0, -1)].index((self.dx, self.dy))

	def move(self, steps):
		for _ in range(steps):
			nextFace = self.face
			nx, ny = self.x + self.dx, self.y + self.dy

			if not (0 <= nx < self.cube.sideLength and 0 <= ny < self.cube.sideLength):
				nextFace = self.face.connections[(self.dx, self.dy)]
				nx, ny = nx % self.cube.sideLength, ny % self.cube.sideLength

			if nextFace.grid[ny][nx] == '#':
				break

			self.face = nextFace
			self.x, self.y = nx, ny

	def turnLeft(self):
		self.dx, self.dy = self.dy, -self.dx

	def turnRight(self):
		self.dx, self.dy = -self.dy, self.dx


def getPassword(board, path):
	cube = Cube(board)
	position = Position(cube, cube.topLeftFace, (0, 0), (1, 0))

	for instruction in path:
		match instruction:
			case 'L':    position.turnLeft()
			case 'R':    position.turnRight()
			case steps:  position.move(int(steps))

	return position.getPassword()


if __name__ == '__main__':
	boardLines, pathLine = sys.stdin.read().split('\n\n')
	board = list(map(str.rstrip, boardLines.splitlines()))
	path = re.findall(r'\d+|L|R', pathLine)

	print(getPassword(board, path))
