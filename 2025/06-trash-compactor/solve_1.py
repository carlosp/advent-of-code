#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

def parseOperands(worksheet: list[str]) -> tuple[tuple[int]]:
	numbers = [tuple(map(int, row.split())) for row in worksheet]

	return tuple(zip(*numbers))

def calculateGrandTotal(worksheet: list[str]) -> int:
	problems = zip(worksheet[-1].split(), parseOperands(worksheet[:-1]))
	operatorFn = {
		'+': sum,
		'*': math.prod
	}

	return sum(operatorFn[operator](operands) for operator, operands in problems)


if __name__ == '__main__':
	print(calculateGrandTotal(sys.stdin.readlines()))
