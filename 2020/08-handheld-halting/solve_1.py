#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

OP_ACC = 'acc'
OP_NOP = 'nop'
OP_JMP = 'jmp'

def parseInstruction(rawInstruction):
	op, value = rawInstruction.split(' ')

	return op, int(value)

def solve(rawInstructions):
	instructions = list(map(parseInstruction, rawInstructions))
	visited = [False] * len(instructions)
	currentIdx, currentAccum = 0, 0

	while not visited[currentIdx]:
		visited[currentIdx] = True
		op, value = instructions[currentIdx]

		if op == OP_ACC:
			currentAccum += value
		elif op == OP_JMP:
			currentIdx += value - 1

		currentIdx += 1

	return currentAccum


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
