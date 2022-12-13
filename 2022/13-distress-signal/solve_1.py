#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

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

def countPacketsInRightOrder(pairsOfPackets):
	return sum(idx for idx, pair in enumerate(pairsOfPackets, 1) if compare(*pair) < 0)


if __name__ == '__main__':
	packets = [eval(line) for line in map(str.strip, sys.stdin.readlines()) if line]

	print(countPacketsInRightOrder(zip(*(iter(packets),) * 2)))
