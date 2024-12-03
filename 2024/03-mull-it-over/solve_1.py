#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def processMemory(memory: str) -> int:
	pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

	return sum(int(n1) * int(n2) for n1, n2 in pattern.findall(memory))


if __name__ == '__main__':
	print(processMemory(sys.stdin.read()))
