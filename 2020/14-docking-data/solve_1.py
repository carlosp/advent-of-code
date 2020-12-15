#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def parseMask(instruction):
	mask = instruction.split('=')[1].strip()
	andMask = int(mask.replace('1', '0').replace('X', '1'), 2)
	orMask = int(mask.replace('X', '0'), 2)

	return andMask, orMask

def parseMemory(instruction):
	left, right = instruction.split('=')
	pos = int(left.split(']')[0][4:])
	value = int(right)

	return pos, value

def solve(instructions):
	(andMask, orMask), mem = (None, None), {}

	for instruction in instructions:
		if instruction.startswith('mask'):
			andMask, orMask = parseMask(instruction)
		elif instruction.startswith('mem'):
			pos, value = parseMemory(instruction)
			mem[pos] = (value & andMask) | orMask

	return sum(mem.values())


if __name__ == '__main__':
	print(solve(map(str.strip, sys.stdin.readlines())))
