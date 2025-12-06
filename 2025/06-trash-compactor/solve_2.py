#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
import sys

def parseOperands(worksheet: list[str]) -> tuple[tuple[int]]:
	columns = tuple(''.join(column).strip() for column in zip(*worksheet))

	return tuple(
		tuple(map(int, group))
		for key, group in itertools.groupby(columns, lambda column: column == '')
		if not key
	)

def calculateGrandTotal(worksheet: list[str]) -> int:
	problems = zip(worksheet[-1].split(), parseOperands(worksheet[:-1]))
	operatorFn = {
		'+': sum,
		'*': math.prod
	}

	return sum(operatorFn[operator](operands) for operator, operands in problems)


if __name__ == '__main__':
	print(calculateGrandTotal(sys.stdin.readlines()))
