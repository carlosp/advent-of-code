#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from dataclasses import dataclass

BOX_WIDTH = 2

@dataclass(unsafe_hash=True)
class Box:
	position: complex
	width: int

	def getGpsCoordinate(self) -> int:
		return int(100 * self.position.real + self.position.imag)

	def getOccupiedPositions(self) -> set[tuple[complex]]:
		return set(self.position + i * 1j for i in range(self.width))

	def getPositionsAfterMove(self, direction: complex) -> set[tuple[complex]]:
		return set(self.position + i * 1j + direction for i in range(self.width)) - set(self.getOccupiedPositions())

	def move(self, direction: complex) -> None:
		self.position += direction


def canMove(walls: set[complex], boxes: dict[complex, Box], position: complex, direction: complex, movedBoxes: set[Box]) -> bool:
	if position in walls:
		return False
	elif position not in boxes:
		return True

	movedBoxes.add(currentBox := boxes[position])

	return all(
		canMove(walls, boxes, movedPosition, direction, movedBoxes)
		for movedPosition in currentBox.getPositionsAfterMove(direction)
	)

def solve(warehouse: list[str], moves: str) -> int:
	walls, boxes, currentPosition = set(), {}, None

	for row in range(len(warehouse)):
		for col in range(len(warehouse[row])):
			position = complex(row, col)

			if warehouse[row][col] == '#':
				walls.add(position)
			elif warehouse[row][col] == '[':
				boxes[position] = boxes[position + 1j] = Box(position=position, width=BOX_WIDTH)
			elif warehouse[row][col] == '@':
				currentPosition = position

	for move in moves:
		direction = {
			'^': -1,
			'v': 1,
			'<': -1j,
			'>': 1j
		}[move]

		if canMove(walls, boxes, currentPosition + direction, direction, movedBoxes := set()):
			currentPosition += direction

			for box in movedBoxes:
				for position in box.getOccupiedPositions():
					del boxes[position]

			for box in movedBoxes:
				box.move(direction)

				for position in box.getOccupiedPositions():
					boxes[position] = box

	return sum(map(Box.getGpsCoordinate, boxes.values())) // BOX_WIDTH


if __name__ == '__main__':
	warehouse, moves = sys.stdin.read().split('\n\n')
	warehouse = [row.replace('.', '..').replace('@', '@.').replace('#', '##').replace('O', '[]') for row in warehouse.splitlines()]

	print(solve(warehouse, moves.replace('\n', '')))
