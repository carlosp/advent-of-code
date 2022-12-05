#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def parseDrawing(drawing):
	numStacks = (1 + len(drawing[0])) // 4
	stacks = [[] for _ in range(numStacks)]

	for line in drawing[-2::-1]:
		for stackIdx in range(numStacks):
			if (crate := line[4 * stackIdx + 1]) != ' ':
				stacks[stackIdx].append(crate)

	return stacks

def applyInstructions(stacks, instructions):
	for _, quantity, _, fromStack, _, toStack in map(str.split, instructions):
		quantity, fromStack, toStack = int(quantity), int(fromStack) - 1, int(toStack) - 1

		stacks[toStack].extend(stacks[fromStack][-quantity:])
		del stacks[fromStack][-quantity:]

	return stacks

def solve(drawing, instructions):
	stacks = applyInstructions(parseDrawing(drawing), instructions)

	return(''.join(stack[-1] for stack in stacks))


if __name__ == '__main__':
	drawing, instructions = map(str.splitlines, sys.stdin.read().split('\n\n'))

	print(solve(drawing, instructions))
