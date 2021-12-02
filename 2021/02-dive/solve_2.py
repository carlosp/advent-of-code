#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(commands):
	horizontalPosition = 0
	depth = 0
	aim = 0

	for command in commands:
		match command:
			case 'forward', x:
				horizontalPosition += x
				depth += aim * x
			case 'down', x:
				aim += x
			case 'up', x:
				aim -= x

	return horizontalPosition * depth

if __name__ == '__main__':
	commands = map(
		lambda x: (x[0], int(x[1])),
		map(str.split, sys.stdin.readlines())
	)
	print(solve(commands))
