#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from textwrap import wrap

CRT_WIDTH = 40
INSTRUCTIONS = {
	'noop': (1, lambda x, _: x),
	'addx': (2, lambda x, v: x + int(v))
}

def getOutput(program):
	cycle, x, result = 0, 1, ''

	for line in program:
		numCycles, updateFn = INSTRUCTIONS[line[0]]

		for _ in range(numCycles):
			cycle += 1
			result += ['.', '█'][x - 1 <= (cycle - 1) % CRT_WIDTH <= x + 1]

		x = updateFn(x, line[-1])

	return '\n'.join(wrap(result, CRT_WIDTH))


if __name__ == '__main__':
	program = [
		line.strip().split()
		for line in sys.stdin.readlines()
	]

	print(getOutput(program))
