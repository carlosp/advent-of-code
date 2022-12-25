#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import itertools
import sys

VALUES = {
	'=': -2,
	'-': -1,
	'0': 0,
	'1': 1,
	'2': 2
}
DIGITS = { value: key for key, value in VALUES.items() }

def addSnafuNumbers(number1, number2):
	result, carry = [], 0

	for digit1, digit2 in itertools.zip_longest(reversed(number1), reversed(number2), fillvalue='0'):
		value, carry = VALUES[digit1] + VALUES[digit2] + carry, 0

		if value < -2:
			value += 5
			carry = -1
		elif value > 2:
			value -= 5
			carry = 1

		result += [value]

	return ''.join(map(DIGITS.get, reversed(result + [1] if carry else result)))


if __name__ == '__main__':
    fuelRequirements = list(map(str.strip, sys.stdin.readlines()))

    print(functools.reduce(addSnafuNumbers, fuelRequirements))
