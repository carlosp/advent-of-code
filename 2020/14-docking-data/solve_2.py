#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def parseMask(instruction):
	mask = instruction.split('=')[1].strip()
	andMask = int(mask.replace('0', '1').replace('X', '0'), 2)
	orMasks, queue, maskSize = [], [(0, mask)], len(mask)

	while queue:
		pos, mask = queue.pop()

		completeMask = True
		for i in range(pos, maskSize):
			if mask[i] == 'X':
				queue += [(i + 1, mask[:i] + '0' + mask[i+1:])]
				queue += [(i + 1, mask[:i] + '1' + mask[i+1:])]
				completeMask = False
				break

		if completeMask:
			orMasks += [int(mask, 2)]

	return andMask, orMasks

def parseMemory(instruction):
	left, right = instruction.split('=')
	pos = int(left.split(']')[0][4:])
	value = int(right)

	return pos, value

def solve(instructions):
	(andMask, orMasks), mem = (None, None), {}

	for instruction in instructions:
		if instruction.startswith('mask'):
			andMask, orMasks = parseMask(instruction)
		elif instruction.startswith('mem'):
			pos, value = parseMemory(instruction)
			for maskedPos in ((pos & andMask) | orMask for orMask in orMasks):
				mem[maskedPos] = value

	return sum(mem.values())


if __name__ == '__main__':
	print(solve(map(str.strip, sys.stdin.readlines())))
