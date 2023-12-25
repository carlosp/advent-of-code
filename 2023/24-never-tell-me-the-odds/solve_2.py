#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]

	result = 0
	for row in range(len(matrix)):
		submatrix = [matrix[row2][1:] for row2 in range(len(matrix)) if row != row2]
		result += [1, -1][row % 2] * matrix[row][0] * determinant(submatrix)

	return result

def buildSystemOfEquations(hailstone1, hailstone2):
	x1, y1, z1, vx1, vy1, vz1 = hailstone1
	x2, y2, z2, vx2, vy2, vz2 = hailstone2

	return (
		[
			[        0, vz2 - vz1, vy1 - vy2,       0, z1 - z2, y2 - y1],
			[vz1 - vz2,         0, vx2 - vx1, z2 - z1,       0, x1 - x2],
			[vy2 - vy1, vx1 - vx2,         0, y1 - y2, x2 - x1,       0]

		],
		[
			z1 * vy1 + y2 * vz2 - y1 * vz1 - z2 * vy2,
			x1 * vz1 + z2 * vx2 - z1 * vx1 - x2 * vz2,
			y1 * vx1 + x2 * vy2 - x1 * vy1 - y2 * vx2
		]
	)

def solveByCramer(a, b):
	d = determinant(a)

	return [
		determinant([a[row][:col] + [b[row]] + a[row][col + 1:] for row in range(len(a))]) // d
		for col in range(3)
	]

def solve(hailstones):
	a1, b1 = buildSystemOfEquations(hailstones[0], hailstones[1])
	a2, b2 = buildSystemOfEquations(hailstones[0], hailstones[2])

	return sum(solveByCramer(a1 + a2, b1 + b2))


if __name__ == '__main__':
	hailstones = [list(map(int, line.replace(',', '').replace('@', '').split())) for line in sys.stdin.readlines()]

	print(solve(hailstones))
