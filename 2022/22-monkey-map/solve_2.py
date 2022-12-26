#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import operator
import re
import sys

U = 'U'
F = 'F'
L = 'L'
R = 'R'
D = 'D'
B = 'B'

CLOCKWISE_FACE_CONNECTIONS = {
	U: [B, R, F, L],
	F: [U, R, D, L],
	L: [U, F, D, B],
	R: [U, B, D, F],
	D: [F, R, B, L],
	B: [U, L, D, R]
}

class Face(object):
	def __init__(self, id, grid, boardPosition):
		self.id = id
		self.grid = grid
		self.boardPosition = boardPosition
		self.connections = {}

	def connect(self, direction, otherFaceId):
		clockwiseConnections = CLOCKWISE_FACE_CONNECTIONS[self.id]
		idx = clockwiseConnections.index(otherFaceId)
		dx, dy = direction

		for i in range(4):
			self.connections[(dx, dy)] = clockwiseConnections[(idx + i) % 4]
			dx, dy = -dy, dx

class Cube(object):
	def __init__(self, board):
		self.board = board
		self.sideLength = math.gcd(len(board), max(len(row) for row in board))
		self.faces = {}
		self.topLeftFace = None

		for x in range(0, len(board[0]), self.sideLength):
			if face := self._parseFace(U, (x, 0), (0, -1), B):
				self.topLeftFace = face
				break

	def _parseFace(self, faceId, position, direction, otherFaceId):
		if faceId not in self.faces:
			boardX, boardY = position

			if 0 <= boardY < len(self.board) and 0 <= boardX < len(self.board[boardY]) and self.board[boardY][boardX] != ' ':
				faceGrid = [row[boardX:boardX + self.sideLength] for row in self.board[boardY:boardY + self.sideLength]]
				self.faces[faceId] = face = Face(faceId, faceGrid, (boardX, boardY))
				face.connect(direction, otherFaceId)

				for (dx, dy), nextFaceId in face.connections.items():
					self._parseFace(nextFaceId, (boardX + dx * self.sideLength, boardY + dy * self.sideLength), (-dx, -dy), faceId)

				return face

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
			ndx, ndy = self.dx, self.dy

			if not (0 <= nx < self.cube.sideLength and 0 <= ny < self.cube.sideLength):
				nextFace = self.cube.faces[self.face.connections[(self.dx, self.dy)]]
				nx, ny = nx % self.cube.sideLength, ny % self.cube.sideLength

				while nextFace.connections[(-ndx, -ndy)] != self.face.id:
					nx, ny = self.cube.sideLength - 1 - ny, nx
					ndx, ndy = -ndy, ndx

			if nextFace.grid[ny][nx] == '#':
				break

			self.face = nextFace
			self.x, self.y = nx, ny
			self.dx, self.dy = ndx, ndy

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
