#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(entries):
	def processEntry(entry):
		_, outputValue = map(str.split, entry.split('|'))

		return sum(len(segments) in [2, 3, 4, 7] for segments in outputValue)

	return sum(map(processEntry, entries))


if __name__ == '__main__':
	entries = sys.stdin.readlines()
	print(solve(entries))
