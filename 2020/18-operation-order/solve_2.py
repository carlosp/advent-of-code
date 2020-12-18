#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

def solveNoParenthesis(expression):
	return math.prod(map(
		lambda sumsExpression: sum(map(int, sumsExpression.split('+'))),
		expression.split('*')))

def solve(expression):
	for idx in range(0, len(expression)):
		if expression[idx] == '(':
			end, level = idx + 1, 1

			while level > 0:
				if expression[end] == '(':
					level += 1
				elif expression[end] == ')':
					level -= 1

				end += 1

			return solve(expression[:idx] + str(solve(expression[idx + 1:end - 1])) + expression[end:])

	return solveNoParenthesis(expression)


if __name__ == '__main__':
	print(sum(map(solve, sys.stdin.readlines())))
