#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

INSTRUCTIONS = {
	'noop': (1, lambda x, _: x),
	'addx': (2, lambda x, v: x + int(v))
}

def getSumOfSignalStrengths(program):
	cycle, x, result = 0, 1, 0

	for line in program:
		numCycles, updateFn = INSTRUCTIONS[line[0]]

		for _ in range(numCycles):
			cycle += 1

			if cycle == 20 or (cycle - 20) % 40 == 0:
				result += cycle * x

		x = updateFn(x, line[-1])

	return result


if __name__ == '__main__':
	program = [
		line.strip().split()
		for line in sys.stdin.readlines()
	]

	print(getSumOfSignalStrengths(program))
