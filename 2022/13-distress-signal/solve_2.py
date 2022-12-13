#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
from functools import cmp_to_key

DIVIDER_PACKETS = [[[2]], [[6]]]

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int):
		return left - right
	elif isinstance(left, int):
		left = [left]
	elif isinstance(right, int):
		right = [right]

	for leftItem, rightItem in zip(left, right):
		if result := compare(leftItem, rightItem):
			return result

	return len(left) - len(right)

def getDecoderKey(packets):
	distressSignal = sorted(packets, key=cmp_to_key(compare))

	return math.prod(idx for idx, packet in enumerate(distressSignal, 1) if packet in DIVIDER_PACKETS)


if __name__ == '__main__':
	packets = [eval(line) for line in map(str.strip, sys.stdin.readlines()) if line]

	print(getDecoderKey(packets + DIVIDER_PACKETS))
