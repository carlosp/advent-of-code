#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

OP_ACC = 'acc'
OP_NOP = 'nop'
OP_JMP = 'jmp'

def parseInstruction(rawInstruction):
	op, value = rawInstruction.split(' ')

	return op, int(value)

def executeInstructions(instructions):
	visited = [False] * len(instructions)
	currentIdx, currentAccum = 0, 0

	while currentIdx < len(instructions) and not visited[currentIdx]:
		visited[currentIdx] = True
		op, value = instructions[currentIdx]

		if op == OP_ACC:
			currentAccum += value
		elif op == OP_JMP:
			currentIdx += value - 1

		currentIdx += 1

	return currentIdx == len(instructions), currentAccum

def solve(rawInstructions):
	instructions = list(map(parseInstruction, rawInstructions))

	for idx, (op, value) in enumerate(instructions):
		if op == OP_NOP:
			instructions[idx] = (OP_JMP, value)
		elif op == OP_JMP:
			instructions[idx] = (OP_NOP, value)

		finished, acum = executeInstructions(instructions)
		instructions[idx] = (op, value)

		if finished:
			return acum


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
