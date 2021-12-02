#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(commands):
	horizontalPosition = 0
	depth = 0

	for command in commands:
		match command:
			case 'forward', x:
				horizontalPosition += x
			case 'down', x:
				depth += x
			case 'up', x:
				depth -= x

	return horizontalPosition * depth

if __name__ == '__main__':
	commands = map(
		lambda x: (x[0], int(x[1])),
		map(str.split, sys.stdin.readlines())
	)
	print(solve(commands))
