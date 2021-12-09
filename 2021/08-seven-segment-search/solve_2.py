#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(entries):
	def processEntry(entry):
		findPattern = lambda size, contains=set(), containedIn=set('abcdefg'), exclude=[]: next(
			pattern for pattern in signalPatterns
			if len(pattern) == size and pattern > contains and pattern <= containedIn
				and all(pattern != other for other in exclude)
		)

		signalPatterns, outputValue = [list(map(set, x)) for x in map(str.split, entry.split('|'))]
		mappings = [None] * 10
		mappings[1] = findPattern(size=2)
		mappings[4] = findPattern(size=4)
		mappings[7] = findPattern(size=3)
		mappings[8] = findPattern(size=7)
		mappings[3] = findPattern(size=5, contains=mappings[1])
		mappings[9] = findPattern(size=6, contains=mappings[3])
		mappings[5] = findPattern(size=5, containedIn=mappings[9], exclude=[mappings[3]])
		mappings[2] = findPattern(size=5, exclude=[mappings[3], mappings[5]])
		mappings[6] = findPattern(size=6, contains=mappings[5], exclude=[mappings[9]])
		mappings[0] = findPattern(size=6, exclude=[mappings[6], mappings[9]])

		return int(''.join(map(str, map(mappings.index, outputValue))))

	return sum(map(processEntry, entries))


if __name__ == '__main__':
	entries = sys.stdin.readlines()
	print(solve(entries))
