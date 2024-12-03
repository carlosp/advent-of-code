#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def processMemory(memory: str) -> int:
	pattern = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)')
	isMulEnabled = True
	result = 0

	for match in pattern.findall(memory):
		match match:
			case ('do()', *_): 			isMulEnabled = True
			case (_, "don't()", *_):	isMulEnabled = False
			case (_, _, n1, n2):		result += isMulEnabled * int(n1) * int(n2)

	return result


if __name__ == '__main__':
	print(processMemory(sys.stdin.read()))
