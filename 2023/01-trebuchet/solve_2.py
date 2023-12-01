#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import sys

DIGIT_STRINGS = {
	**{ char: int(char) for char in string.digits[1:] },
	'one'	: 1,
	'two'	: 2,
	'three'	: 3,
	'four'	: 4,
	'five'	: 5,
	'six'	: 6,
	'seven'	: 7,
	'eight'	: 8,
	'nine'	: 9
}

def getCalibrationValue(line):
	firstDigit, firstIdx = None, len(line)
	lastDigit, lastIdx = None, -1

	for digitString, digitValue in DIGIT_STRINGS.items():
		if 0 <= (idx := line.find(digitString)) < firstIdx:
			firstDigit, firstIdx = digitValue, idx

		if 0 <= (idx := line.rfind(digitString)) > lastIdx:
			lastDigit, lastIdx = digitValue, idx

	return 10 * firstDigit + lastDigit


if __name__ == '__main__':
	print(sum(map(getCalibrationValue, sys.stdin.readlines())))
