#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def runProgramAndGetOutput(program: list[int], a: int, b: int, c: int) -> list[int]:
	combo = lambda operand: [0, 1, 2, 3, a, b, c][operand]
	ip, output = 0, []

	while ip < len(program):
		opcode, operand = program[ip], program[ip + 1]
		ip += 2

		match opcode:
			case 0: a //= 2 ** combo(operand)
			case 1: b ^= operand
			case 2: b = combo(operand) % 8
			case 3: ip = [operand, ip][not a]
			case 4: b ^= c
			case 5: output.append(combo(operand) % 8)
			case 6: b = a // (2 ** combo(operand))
			case 7: c = a // (2 ** combo(operand))

	return output

def solve(program: list[int], b: int, c: int) -> int:
	queue = [(len(program) - 1, 0)]

	while queue:
		idx, a = queue.pop()

		if idx == -1:
			return a

		for candidate in range(7, -1, -1):
			if runProgramAndGetOutput(program, nextA := 8 * a + candidate, b, c) == program[idx:]:
				queue.append((idx - 1, nextA))


if __name__ == '__main__':
	_, b, c, *program = map(int, re.findall(r'\d+', sys.stdin.read()))

	print(solve(program, b, c))
