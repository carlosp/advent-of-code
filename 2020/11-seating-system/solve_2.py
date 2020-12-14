#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def occupiedSeatsOverLimit(seats, height, width, row, col, limit):
	occupiedSeats = 0

	for dx, dy in DIRECTIONS:
		x, y = row, col

		while True:
			x, y = x + dx, y + dy

			if not (0 <= x < height and 0 <= y < width):
				break

			if seats[x][y] != FLOOR:
				occupiedSeats += seats[x][y] == OCCUPIED

				if occupiedSeats > limit:
					return True

				break

	return False

def iterate(seats, newSeats, height, width):
	changed = False

	for row in range(height):
		for col in range(width):
			seat = seats[row][col]

			if seat == EMPTY and not occupiedSeatsOverLimit(seats, height, width, row, col, 0):
				state = OCCUPIED
				changed = True
			elif seat == OCCUPIED and occupiedSeatsOverLimit(seats, height, width, row, col, 4):
				state = EMPTY
				changed = True
			else:
				state = seat

			newSeats[row][col] = state

	return newSeats, seats, changed

def solve(seats):
	height, width = len(seats), len(seats[0])
	newSeats = [[None] * width for _ in range(height)]
	changed = True

	while changed:
		seats, newSeats, changed = iterate(seats, newSeats, height, width)

	return sum(row.count(OCCUPIED) for row in seats)


if __name__ == '__main__':
	print(solve(list(map(lambda x: list(x.strip()), sys.stdin.readlines()))))
