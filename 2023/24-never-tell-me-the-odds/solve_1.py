#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MIN_POSITION = 200000000000000
MAX_POSITION = 400000000000000

def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]

	result = 0
	for row in range(len(matrix)):
		submatrix = [matrix[row2][1:] for row2 in range(len(matrix)) if row != row2]
		result += [1, -1][row % 2] * matrix[row][0] * determinant(submatrix)

	return result

def buildSystemOfEquations(hailstone1, hailstone2):
	x1, y1, _, vx1, vy1, _ = hailstone1
	x2, y2, _, vx2, vy2, _ = hailstone2

	return (
		[
			[vx1, -vx2],
			[vy1, -vy2]
		],
		[
			x2 - x1,
			y2 - y1
		]
	)

def solveByCramer(a, b):
	if d := determinant(a):
		return [
			determinant([a[row][:col] + [b[row]] + a[row][col + 1:] for row in range(len(a))]) / d
			for col in range(2)
		]

def solve(hailstones):
	result = 0

	for idx1, hailstone1 in enumerate(hailstones):
		for hailstone2 in hailstones[:idx1]:
			a, b = buildSystemOfEquations(hailstone1, hailstone2)

			if intersectionTimes := solveByCramer(a, b):
				t1, t2 = intersectionTimes

				if t1 > 0 and t2 > 0:
					x = hailstone1[0] + t1 * hailstone1[3]
					y = hailstone1[1] + t1 * hailstone1[4]
					result += MIN_POSITION <= x <= MAX_POSITION and MIN_POSITION <= y <= MAX_POSITION


	return result


if __name__ == '__main__':
	hailstones = [list(map(int, line.replace(',', '').replace('@', '').split())) for line in sys.stdin.readlines()]

	print(solve(hailstones))
